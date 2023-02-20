import random

from loguru import logger
from requests import Response

from app.src.generated_data.generator import generated_store_data


class StoreModule:

    def __init__(self, app):
        self.app = app
        self.endpoint = '/store'
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.created_stores_order_id = None

    def create_store_order(self) -> Response:
        """ https://petstore.swagger.io/#/store/placeOrder """

        generated_data = next(generated_store_data())
        data = {
            'petId': f'{generated_data.petId}',
            'quantity': f'{generated_data.quantity}',
            'shipDate': f'{generated_data.shipDate}',
            'status': f'{generated_data.status}',
            'complete': f'{generated_data.complete}'
        }

        logger.info(f'Payload: {data}')

        r = self.app.common.post_req(endpoint=f'{self.endpoint}/order', headers=self.headers, data=data)
        self.created_stores_order_id = r.json()['id']

        logger.info(f'Created stores order ID: {self.created_stores_order_id}')

        return r

    def get_order_by_id(self) -> Response:
        """ https://petstore.swagger.io/#/store/getOrderById """

        return self.app.common.get_req(endpoint=f'{self.endpoint}/order/{random.randint(1, 10)}', headers=self.headers)

    def delete_order(self) -> Response:
        """ https://petstore.swagger.io/#/store/deleteOrder """

        return self.app.common.delete_req(
            endpoint=f'{self.endpoint}/order/{self.created_stores_order_id}',
            headers=self.headers
        )

    def get_inventory(self) -> Response:
        """ https://petstore.swagger.io/#/store/getInventory """

        return self.app.common.get_req(endpoint=f'{self.endpoint}/inventory', headers=self.headers)
