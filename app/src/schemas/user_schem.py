from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class SuccessfulRequestModel(BaseModel):
    code: int = 200
    type: str
    message: str

    @field_validator('code')
    def validate_code_value(cls, code):
        if code != 200:
            raise ValueError('Code value should be equal 200')
