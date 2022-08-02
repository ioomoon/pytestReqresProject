"""
Fixtures — это функции, выполняемые pytest до (а иногда и после) фактических тестовых функций.
"""

import pytest
import requests

from configuration import *


@pytest.fixture()
def get_users():
    response = requests.get(url=SERVICE_URL + USERS)
    return response


@pytest.fixture()
def get_user():
    response = requests.get(url=SERVICE_URL + USER)
    return response


@pytest.fixture()
def get_null_user():
    response = requests.get(url=SERVICE_URL + NULL_USER)
    return response
