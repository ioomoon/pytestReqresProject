import pytest
import allure

from src.baseclasses.Response import Response

from src.enums.global_enums import *
from src.pydantic_schemas.user import User


@pytest.mark.development
@allure.severity(allure.severity_level.CRITICAL)
def test_status_getting_users(get_users):
    """
    Проверка статус-кода запроса пользователей
    :param get_users:
    :return:
    """
    Response(get_users).assert_status_code(200)


@pytest.mark.development
@allure.severity(allure.severity_level.CRITICAL)
def test_status_getting_user(get_user):
    """
    Проверка статус-кода запроса конкретного пользователя
    :param get_user:
    :return:
    """
    Response(get_user).assert_status_code(200)


@pytest.mark.skip
@pytest.mark.development
@allure.severity(allure.severity_level.CRITICAL)
def test_status_getting_null_user(get_null_user):
    """
    Проверка статус-кода запроса несуществующего пользователя
    :param get_null_user:
    :return:
    """
    Response(get_null_user).assert_status_code(404)


@pytest.mark.development
@pytest.mark.production
@allure.severity(allure.severity_level.CRITICAL)
def test_count_getting_users(get_users):
    """
    Проверка количества пользователей, полученных при запросе
    :param get_users:
    :return:
    """
    received_users_data = Response(get_users).response_json

    assert len(received_users_data) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


# def test_validate_user_data_with_jsonschema():
#     r = requests.get(url=SERVICE_URL + GET_USER)
#     response = Response(r)
#
#     response.validate(USER_SCHEMA)


@pytest.mark.development
@pytest.mark.production
@allure.severity(allure.severity_level.NORMAL)
def test_validate_user_data_with_pydantic(get_user):
    """
    Валидация полей
    :param get_user:
    :return:
    """
    Response(get_user).validate(User)
