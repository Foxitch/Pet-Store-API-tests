from pydantic import BaseModel


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


class StoresInventoryModel(BaseModel):
    sold: int
    string: int
    available: int
