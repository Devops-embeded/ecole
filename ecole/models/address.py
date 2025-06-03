# -*- coding: utf-8 -*-
from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    postal_code: int
    def __str__(self) -> str:
        return f"{self.street}, {self.city} {self.postal_code}"