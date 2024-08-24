from dataclasses import dataclass
from typing import Self, Generic, TypeVar

ItemT = TypeVar("ItemT")


@dataclass
class Token(Generic[ItemT]):
    item: ItemT | None
    predecessor: Self

    def __init__(self, item: ItemT | None = None, predecessor: Self | None = None):
        self.item = item
        if predecessor is None:
            self.predecessor = self
        else:
            self.predecessor = predecessor

    def __iter__(self):
        return TokenIterator(self)


class TokenIterator(Generic[ItemT]):
    def __init__(self, token: Token[ItemT]) -> None:
        self.pointer = token

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> ItemT:
        if self.pointer.item is None:
            raise StopIteration
        item = self.pointer.item
        self.pointer = self.pointer.predecessor
        return item


class Stack(Generic[ItemT]):
    def __init__(self, item: ItemT | None = None) -> None:
        self.__token = Token[ItemT]()
        if item is not None:
            self.append(item)

    def is_empty(self):
        return self.__token.item is None

    def get(self) -> ItemT:
        if self.__token.item is None:
            raise IndexError("get from empty stack")
        return self.__token.item

    def append(self, item: ItemT) -> None:
        self.__token = Token(item, self.__token)

    def pop(self) -> ItemT:
        if self.__token.item is None:
            raise IndexError("pop from empty stack")
        item = self.__token.item
        self.__token = self.__token.predecessor
        return item

    def __iter__(self) -> Token[ItemT]:
        return iter(self.__token)

    def __repr__(self) -> str:
        if self.is_empty():
            return "]-("
        iterator = iter(self)
        representation = f"{next(iterator)!r}]"
        for item in iterator:
            representation = f"{item!r}]-(" + representation
        return "]-(" + representation
