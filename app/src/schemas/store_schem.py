from pydantic import BaseModel, field_validator


class StoreModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool


class DeletedStoresOrderModel(BaseModel):
    code: int = 200
    type: str
    message: str

    @field_validator('code')
    def validate_code_value(cls, code):
        if code != 200:
            raise ValueError('Code value should be equal 200')


class StoresInventoryModel(BaseModel):
    sold: int
    string: int
    available: int
