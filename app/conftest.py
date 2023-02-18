import pytest

from app.modules.application import Application


@pytest.fixture(scope='session')
def app() -> Application:
    fixture = Application()
    return fixture
