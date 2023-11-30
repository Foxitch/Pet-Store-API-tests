from requests import Response

from app.src.generated_data.generator import generated_pet_data


class PetModule:

    def __init__(self, app):
        self.app = app
        self.endpoint = '/pet'
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.created_pet_id = None

    def create_pet(self) -> Response:
        """ https://petstore.swagger.io/#/pet/addPet """

        generate_data = next(generated_pet_data())
        payload = {
            'category': {
                'name': f'{generate_data.name}'
            },
            'name': f'{generate_data.name}',
            'photoUrls': [
                'string'
            ],
            'tags': [
                {
                    'name': f'{generate_data.name}'
                }
            ],
            'status': f'{generate_data.status}'
        }

        r = self.app.api_base.session_request(
            method='POST',
            endpoint=self.endpoint,
            headers=self.headers,
            payload=payload
        )
        self.created_pet_id = r.json()['id']

        return r

    def get_pet_by_id(self) -> Response:
        """ https://petstore.swagger.io/#/pet/getPetById """

        return self.app.api_base.session_request(
            method='GET',
            endpoint=f'{self.endpoint}/{self.created_pet_id}',
            headers=self.headers
        )

    def change_pet_info(self) -> Response:
        """ https://petstore.swagger.io/#/pet/updatePet """

        generate_data = next(generated_pet_data())
        payload = {
            'category': {
                'name': f'{generate_data.name}'
            },
            'name': f'{generate_data.name}',
            'photoUrls': [
                'string'
            ],
            'tags': [
                {
                    'name': f'{generate_data.name}'
                }
            ],
            'status': f'{generate_data.status}'
        }

        return self.app.api_base.session_request(
            method='PUT',
            endpoint=f'{self.endpoint}/{self.created_pet_id}',
            headers=self.headers,
            payload=payload
        )

    def find_pets_by_status(self) -> tuple[Response, str]:
        """ https://petstore.swagger.io/#/pet/findPetsByStatus """

        status: str = next(generated_pet_data()).status
        return self.app.api_base.session_request(
            method='GET',
            endpoint=f'{self.endpoint}/findByStatus',
            params={'status': f'{status}'},
            headers=self.headers
        ), status

    def delete_pet(self) -> Response:
        """ https://petstore.swagger.io/#/pet/deletePet """

        return self.app.api_base.session_request(
            method='DELETE',
            endpoint=f'{self.endpoint}/{self.created_pet_id}',
            headers=self.headers
        )
