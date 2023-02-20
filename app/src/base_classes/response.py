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
    def validate_schem(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code: int):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def assert_pet_status(self, status: str):
        for obj in self.response_json:
            assert obj['status'] == status

    def __str__(self):
        return \
            f'\nStatus code: {self.response_status}\n' \
            f'Request URL: {self.response.url}\n' \
            f'Response body: {self.response_json}\n'
