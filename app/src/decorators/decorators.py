from loguru import logger
from pydantic import ValidationError


def error_handler(func):
    """ Decorator error handler """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            logger.error(f'Error handler: {error}')
            raise error
    return wrapper


def schem_error(func):
    """ Catches json schem validation error and raise AssertionError with error message using JSON format """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as error:
            raise AssertionError(error.json())
    return wrapper
