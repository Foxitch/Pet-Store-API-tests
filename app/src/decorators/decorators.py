from pydantic import ValidationError


def schem_error(func):
    """ Catches json schem validation error and raise AssertionError with error message using JSON format """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as error:
            raise AssertionError(error.json())
    return wrapper
