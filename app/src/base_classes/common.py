import json

from loguru import logger

from app.src.decorators.decorators import error_handler

import requests
from requests import Response


class Common:
    """ Wrapper over the requests library """

    def __init__(self, url: str):
        self.url = url

    @error_handler
    def get_req(self, endpoint: str, headers: dict = None) -> Response:
        r = requests.get(url=self.url + endpoint, headers=headers)
        logger.info(f'Response body: {r.text}')
        return r

    @error_handler
    def post_req(self, endpoint: str, headers: dict = None, data: dict = None) -> Response:
        r = requests.post(url=self.url + endpoint, headers=headers, data=json.dumps(data))
        logger.info(f'Response body: {r.text}')
        return r

    @error_handler
    def put_req(self, endpoint: str, headers: dict = None, data: dict = None) -> Response:
        r = requests.put(url=self.url + endpoint, headers=headers, data=json.dumps(data))
        logger.info(f'Response body: {r.text}')
        return r

    @error_handler
    def patch_req(self, endpoint: str, headers: dict = None, data: dict = None) -> Response:
        r = requests.patch(url=self.url + endpoint, headers=headers, data=json.dumps(data))
        logger.info(f'Response body: {r.text}')
        return r

    @error_handler
    def delete_req(self, endpoint: str, headers: dict = None, data: dict = None) -> Response:
        r = requests.delete(url=self.url + endpoint, headers=headers, data=json.dumps(data))
        logger.info(f'Response body: {r.text}')
        return r
