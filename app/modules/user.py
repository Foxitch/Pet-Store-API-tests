import random

from loguru import logger
from requests import Response

from app.src.generated_data.generator import generated_user_data


class UserModule:

    def __init__(self, app):
        self.app = app
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.created_user_name = None
        self.created_user_password = None

    def create_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/createUser """

        generated_data = next(generated_user_data())
        self.created_user_name = generated_data.username
        self.created_user_password = generated_data.password
        data = {
            'username': f'{self.created_user_name}',
            'firstName': f'{generated_data.username}',
            'lastName': f'{generated_data.lastName}',
            'email': f'{generated_data.email}',
            'password': f'{self.created_user_password}',
            'phone': f'{generated_data.phone}',
            'userStatus': f'{generated_data.userStatus}'
        }

        return self.app.common.post_req(endpoint='/user', headers=self.headers, data=data)

    def get_created_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/getUserByName """

        return self.app.common.get_req(endpoint='/user', headers=self.headers)

    def change_user_info(self) -> Response:
        """ https://petstore.swagger.io/#/user/updateUser """

        generated_data = next(generated_user_data())
        data = {
            'username': f'{self.created_user_name}',
            'firstName': f'{generated_data.username}',
            'lastName': f'{generated_data.lastName}',
            'email': f'{generated_data.email}',
            'password': f'{self.created_user_password}',
            'phone': f'{generated_data.phone}',
            'userStatus': f'{generated_data.userStatus}'
        }

        return self.app.common.put_req(endpoint='/user', headers=self.headers, data=data)
