from dataclasses import dataclass
from typing import Generic, Self
from .types.types import ItemT
from .token import Token
from .sentinel import Sentinel


class StackIterator(Generic[ItemT]):
    def __init__(self, pointer: Token[ItemT] | Sentinel, sentinel: Sentinel) -> None:
        self.pointer = pointer
        self.sentinel = sentinel

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> ItemT:
        if self.pointer is self.sentinel:
            raise StopIteration
        assert isinstance(self.pointer, Token)
        item = self.pointer.item
        self.pointer = self.pointer.predecessor
        return item

    def __repr__(self):
        return f"StackIteratot(pointer={self.pointer!r}, sentinel={self.sentinel!r})"


class Stack(Generic[ItemT]):
    def __init__(self, *items: ItemT) -> None:
        self.__sentinel: Sentinel = Sentinel()
        self.__size = 0
        for item in items:
            self.append(item)

    def get(self) -> ItemT:
        if not self:
            raise IndexError("get from empty stack")
        assert isinstance(self.__sentinel.predecessor, Token)
        return self.__sentinel.predecessor.item

    def append(self, item: ItemT) -> None:
        self.__sentinel.predecessor = Token(item, self.__sentinel.predecessor)
        self.__size += 1

    def pop(self) -> ItemT:
        if not self:
            raise IndexError("pop from empty stack")
        assert isinstance(self.__sentinel.predecessor, Token)
        item = self.__sentinel.predecessor.item
        self.__sentinel.predecessor = self.__sentinel.predecessor.predecessor
        self.__size -= 1
        return item

    def __iter__(self) -> StackIterator[ItemT]:
        return StackIterator(self.__sentinel.predecessor, self.__sentinel)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        if not self:
            return "]-("
        representation = "]"
        for item in self:
            representation = f"]-({item!r}" + representation
        return representation
