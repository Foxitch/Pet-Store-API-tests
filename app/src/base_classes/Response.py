from app.src.decorators.decorators import schem_error


class Response:
    """ Base class for response validation """

    def __init__(self, response):
        self.response = response

        if len(response.text) == 0:
            self.response_json = None
        else:
            self.response_json = response.json()

        self.response_status = response.status_code

    @schem_error
    def validate_response_model(self, response_body: dict | list, schema, expect_error: bool = False) -> None:
        if expect_error:
            return

        if isinstance(response_body, list):
            for obj in response_body:
                schema.model_validate(obj)
            return
        schema.model_validate(response_body)

    def assert_status_code(self, status_code: int) -> None:
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self

    def assert_pet_status(self, status: str) -> None:
        for obj in self.response_json:
            assert obj['status'] == status
