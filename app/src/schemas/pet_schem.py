from typing import Literal

from pydantic import BaseModel, field_validator


class Category(BaseModel):
    id: int
    name: str


class Tags(BaseModel):
    id: int
    name: str


class PetModel(BaseModel):
    id: int
    category: Category = None
    name: str
    photoUrls: list[str]
    tags: list[Tags]
    status: Literal['available', 'pending', 'sold']

    @field_validator('status')
    def validate_code_value(cls, status):
        if status not in ('available', 'pending', 'sold'):
            raise ValueError(f'Status should be on of the {status}')


class DeletedPet(BaseModel):
    code: int = 200
    type: str
    message: str

    @field_validator('code')
    def validate_code_value(cls, code):
        if code != 200:
            raise ValueError('Code value should be equal 200')
