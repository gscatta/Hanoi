from dataclasses import dataclass
from typing import Generic, Self, TypeVar

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


class StackIterator(Generic[ItemT]):
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
    def __init__(self, *items: ItemT) -> None:
        self.__token = Token[ItemT]()
        self.__size = 0
        for item in items:
            self.append(item)

    def is_empty(self) -> bool:
        return self.__token.item is None

    def get(self) -> ItemT:
        if self.__token.item is None:
            raise IndexError("get from empty stack")
        return self.__token.item

    def append(self, item: ItemT) -> None:
        self.__token = Token(item, self.__token)
        self.__size += 1

    def pop(self) -> ItemT:
        if self.__token.item is None:
            raise IndexError("pop from empty stack")
        item = self.__token.item
        self.__token = self.__token.predecessor
        self.__size -= 1
        return item

    def __iter__(self) -> StackIterator[ItemT]:
        return StackIterator(self.__token)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        if self.is_empty():
            return "]-("
        representation = "]"
        for item in self:
            representation = f"]-({item!r}" + representation
        return representation
