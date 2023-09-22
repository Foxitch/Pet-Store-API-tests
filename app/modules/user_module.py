from requests import Response

from app.src.generated_data.generator import generated_user_data


class UserModule:

    def __init__(self, app):
        self.app = app
        self.endpoint = '/user'
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.created_user_name = None
        self.created_user_password = None

    def create_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/createUser """

        generated_data = next(generated_user_data())
        self.created_user_name = generated_data.username
        self.created_user_password = generated_data.password
        payload = {
            'username': f'{self.created_user_name}',
            'firstName': f'{generated_data.username}',
            'lastName': f'{generated_data.lastName}',
            'email': f'{generated_data.email}',
            'password': f'{self.created_user_password}',
            'phone': f'{generated_data.phone}',
            'userStatus': f'{generated_data.userStatus}'
        }

        return self.app.api_base.session_request(
            method='POST',
            endpoint=f'{self.endpoint}',
            headers=self.headers,
            payload=payload
        )

    def get_created_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/getUserByName """

        return self.app.api_base.session_request(
            method='GET',
            endpoint=f'{self.endpoint}/{self.created_user_name}',
            headers=self.headers
        )

    def change_user_info(self) -> Response:
        """ https://petstore.swagger.io/#/user/updateUser """

        generated_data = next(generated_user_data())
        payload = {
            'username': f'{self.created_user_name}',
            'firstName': f'{generated_data.username}',
            'lastName': f'{generated_data.lastName}',
            'email': f'{generated_data.email}',
            'password': f'{self.created_user_password}',
            'phone': f'{generated_data.phone}',
            'userStatus': f'{generated_data.userStatus}'
        }

        return self.app.api_base.session_request(
            method='PUT',
            endpoint=f'{self.endpoint}/{self.created_user_name}',
            headers=self.headers,
            payload=payload
        )

    def login_as_created_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/loginUser """

        return self.app.api_base.session_request(
            method='GET',
            endpoint=f'{self.endpoint}/login',
            params={
                'username': self.created_user_name,
                'password': self.created_user_password
            },
            headers=self.headers
        )

    def delete_user(self) -> Response:
        """ https://petstore.swagger.io/#/user/deleteUser """

        return self.app.api_base.session_request(
            method='DELETE',
            endpoint=f'{self.endpoint}/{self.created_user_name}'
        )

    def create_list_of_users(self) -> Response:
        """ https://petstore.swagger.io/#/user/createUsersWithListInput """

        generated_data_for_user1 = next(generated_user_data())
        generated_data_for_user2 = next(generated_user_data())
        payload = [
            {
                'username': f'{generated_data_for_user1.username}',
                'firstName': f'{generated_data_for_user1.firstName}',
                'lastName': f'{generated_data_for_user1.lastName}',
                'email': f'{generated_data_for_user1.email}',
                'password': f'{generated_data_for_user1.password}',
                'phone': f'{generated_data_for_user1.phone}',
                'userStatus': f'{generated_data_for_user1.userStatus}'
            },
            {
                'username': f'{generated_data_for_user2.username}',
                'firstName': f'{generated_data_for_user2.firstName}',
                'lastName': f'{generated_data_for_user2.lastName}',
                'email': f'{generated_data_for_user2.email}',
                'password': f'{generated_data_for_user2.password}',
                'phone': f'{generated_data_for_user2.phone}',
                'userStatus': f'{generated_data_for_user2.userStatus}'
            }
        ]

        return self.app.api_base.session_request(
            method='POST',
            endpoint=f'{self.endpoint}/createWithList',
            headers=self.headers, payload=payload
        )
