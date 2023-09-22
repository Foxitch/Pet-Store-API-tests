import logging
import requests

from requests import Response


class ApiBase:

    def __init__(self, api_url: str):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.api_url = api_url
        self.requests = requests
        self.session = requests.Session()

    def session_request(self,
                        method: str,
                        url: str,
                        payload: dict | list = None,
                        params: dict | list = None,
                        headers: dict = None,
                        expected_code: int = 200,
                        replace_headers: bool = False,
                        **kwargs) -> Response:

        if headers:
            self.session.headers.update(headers)

        if replace_headers:
            self.session.headers.clear()
            self.session.headers.update(headers)

        response = self.session.request(
            method=method,
            url=url,
            headers=self.session.headers,
            json=payload,
            params=params,
            timeout=10,
            verify=False,
            **kwargs
        )

        self._request_logger(response=response)
        assert response.status_code == int(expected_code), self._request_logger(response=response)

        return response

    def _request_logger(self, response: Response) -> None:
        self.logger.info(f'REQUEST: {response.request.method} {response.request.url}')
        self.logger.info(f'REQUEST PAYLOAD: {response.request.body}')
        self.logger.info(f'REQUEST HEADERS: {response.request.headers}')
        self.logger.info(f'RESPONSE STATUS CODE: {response.status_code}')
        self.logger.info(f'RESPONSE HEADERS: {response.headers}')
        self.logger.info(f'RESPONSE: {response.content.decode("unicode-escape")}')
