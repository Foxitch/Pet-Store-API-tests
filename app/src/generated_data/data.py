from datetime import datetime
from dataclasses import dataclass


@dataclass
class PetData:
    name: str = None
    status: str = None


@dataclass
class StoreData:
    petId: int = None
    quantity: int = None
    shipDate: str = None
    status: str = None
    complete: bool = None
