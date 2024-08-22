"""Module providing Stack and Queue"""

from typing import Self
from dataclasses import dataclass


@dataclass
class Token:
    """class representing a single piece of data in Stack and Queue"""

    item: str | int | float
    link: Self | None = None
    colink: Self | None = None


class Stack:
    """class representing a Stack"""

    def __init__(self, item=None):
        if item:
            self.__last_token = Token(item)
        else:
            self.__last_token = None

    def is_empty(self):
        return self.__last_token is None

    def get(self):
        if self.__last_token is None:
            return None
        return self.__last_token.item

    def pop(self):
        if self.__last_token is None:
            raise IndexError("empty stack")
        item = self.__last_token.item
        self.__last_token = self.__last_token.link
        return item

    def append(self, item):
        self.__last_token = Token(item, self.__last_token)

    def __str__(self):
        if self.__last_token is None:
            return "()"
        if self.__last_token.link is None:
            return f"({self.get()})"
        return f"• <-- ({self.get()})"


class Queue:
    def __init__(self, item=None):
        if item is None:
            self.__first_token = None
            self.__last_token = None
        else:
            token = Token(item)
            self.__first_token = token
            self.__last_token = token

    def get(self):
        if self.__first_token is None:
            return None
        return self.__first_token.item

    def append(self, item):
        token = self.__last_token
        self.__last_token = Token(item, token)
        token.colink = self.__last_token

    def pop(self):
        if self.__first_token is None:
            raise Exception("empty queue")
        item = self.__first_token.item
        self.__first_token = self.__first_token.colink
        return item

    def __str__(self):
        if self.__first_token is None or self.__last_token is None:
            return "()"
        if self.__first_token is self.__last_token:
            return f"({self.__first_token.item})"
        return f"({self.__first_token.item}) <-- ... <-- ({self.__last_token.item})"
