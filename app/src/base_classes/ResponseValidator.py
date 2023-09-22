from requests import Response

from app.src.decorators.decorators import schem_error


class ResponseValidator:
    """ Base class for response validation """

    def __init__(self, response: Response):
        self.response = response

        if len(response.text) == 0:
            self.response_body = None
        else:
            self.response_body = response.json()

        self.response_status = response.status_code

    def validate_status_code(self, expected_status_code: int):
        assert self.response_status == expected_status_code, \
            f'Expected status code is {expected_status_code}, actual is {self.response_status}'
        return self

    @schem_error
    def validate_response_model(self, schema, expect_error: bool = False):
        if expect_error:
            return self

        if isinstance(self.response_body, list):
            for obj in self.response_body:
                schema.model_validate(obj)
            return self
        else:
            schema.model_validate(self.response_body)

        return self

    def assert_pet_status(self, status: str) -> None:
        for obj in self.response_body:
            assert obj['status'] == status
