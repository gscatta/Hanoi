from dataclasses import dataclass
from typing import Self, Generic, TypeVar

ItemT = TypeVar("ItemT")


@dataclass
class Token(Generic[ItemT]):
    item: ItemT | None
    predecessor: Self
    __pointer: Self

    def __init__(self, item: ItemT | None = None, predecessor: Self | None = None):
        self.__pointer = self
        self.item = item
        if predecessor is None:
            self.predecessor = self
        else:
            self.predecessor = predecessor

    def __iter__(self):
        return self

    def __next__(self) -> ItemT:
        if self.__pointer.item is None:
            self.__pointer = self
            raise StopIteration
        item = self.__pointer.item
        self.__pointer = self.__pointer.predecessor
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
        return self.__token

    def __repr__(self) -> str:
        if self.is_empty():
            return "]-("
        representation = f"({next(iter(self))!r}]"
        for item in self:
            representation = f"({item!r}]-" + representation
        return "]-" + representation
