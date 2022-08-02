import pytest
import requests

from configuration import *


@pytest.fixture()
def post_user():
    response = requests.post(SERVICE_URL + USERS, data=TEST_USER)
    return response
