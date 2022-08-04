import pytest
import requests

from src.generators.user import User
from configuration import *


@pytest.fixture()
def post_user(get_user_generator):
    response = requests.post(SERVICE_URL + USERS, data=get_user_generator)
    return response


@pytest.fixture()
def get_user_generator():
    fake_user = User().build()
    print(fake_user)
    return fake_user
