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


@dataclass
class UserData:
    username: str = None
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    phone: str = None
    userStatus: int = None
