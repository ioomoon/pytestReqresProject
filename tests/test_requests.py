import requests

from src.baseclasses.Response import Response

from configuration import *

from src.enums.global_enums import *
from src.json_schemas.user import USER_SCHEMA
from src.pydantic_schemas.user import User


def test_status_getting_users():
    r = requests.get(url=SERVICE_URL + GET_USERS)
    response = Response(r)

    response.assert_status_code(200)


def test_status_getting_user():
    r = requests.get(url=SERVICE_URL + GET_USER)
    response = Response(r)

    response.assert_status_code(200)


def test_status_getting_null_user():
    r = requests.get(url=SERVICE_URL + GET_NULL_USER)
    response = Response(r)

    response.assert_status_code(404)


def test_count_getting_users():
    response = requests.get(url=SERVICE_URL + GET_USERS)
    received_users_data = response.json()

    assert len(received_users_data) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


# def test_validate_user_data_with_jsonschema():
#     r = requests.get(url=SERVICE_URL + GET_USER)
#     response = Response(r)
#
#     response.validate(USER_SCHEMA)
#

def test_validate_user_data_with_pydantic():
    r = requests.get(url=SERVICE_URL + GET_USER)
    response = Response(r)

    response.validate(User)
