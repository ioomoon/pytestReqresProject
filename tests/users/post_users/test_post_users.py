import pytest
import allure
from allure_commons.types import Severity

from src.baseclasses.Response import Response


@pytest.mark.development
@allure.severity(allure.severity_level.CRITICAL)
def test_status_when_post_user(post_user):
    """
    Проверка статус-кода отправки данных пользователя
    :param post_user:
    :return:
    """
    Response(post_user).assert_status_code(201)
