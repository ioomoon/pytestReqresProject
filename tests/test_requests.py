import requests

from src.baseclasses.Response import Response

from configuration import *

from src.enums.global_enums import *
from src.json_schemas.user import USER_SCHEMA
from src.pydantic_schemas.user import User


def test_status_getting_users(get_users):
    Response(get_users).assert_status_code(200)


def test_status_getting_user(get_user):
    Response(get_user).assert_status_code(200)


def test_status_getting_null_user(get_null_user):
    Response(get_null_user).assert_status_code(404)


def test_count_getting_users(get_users):
    received_users_data = Response(get_users).response_json

    assert len(received_users_data) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


# def test_validate_user_data_with_jsonschema():
#     r = requests.get(url=SERVICE_URL + GET_USER)
#     response = Response(r)
#
#     response.validate(USER_SCHEMA)
#

def test_validate_user_data_with_pydantic(get_user):
   Response(get_user).validate(User)
