from dataclasses import dataclass
from typing import Generic, Self, TYPE_CHECKING
from .types.types import ItemT
from .sentinel import Sentinel


@dataclass
class Token(Generic[ItemT]):
    item: ItemT
    predecessor: Self | Sentinel
