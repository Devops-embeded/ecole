from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC
from typing import Optional
from .address import Address

@dataclass
class Person(ABC):
    first_name: str
    last_name: str
    age: int
    address: Optional[Address] = field(default=None, init=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.age} ans)" + \
               (f", {self.address}" if self.address else "")
