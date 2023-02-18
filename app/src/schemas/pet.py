from typing import Literal

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class Tags(BaseModel):
    id: int
    name: str


class PetModel(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tags]
    status: Literal['available', 'pending', 'sold']


class DeletedPet(BaseModel):
    code: int = 200
    type: str
    message: str
