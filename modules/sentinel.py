from dataclasses import dataclass
from typing import Generic, Self, TYPE_CHECKING
from .types.types import ItemT

if TYPE_CHECKING:
    from .token import Token


@dataclass
class Sentinel(Generic[ItemT]):
    predecessor: Self | "Token[ItemT]"

    def __init__(self):
        self.predecessor = self
