from src.baseclasses.Response import Response


def test_status_when_post_user(post_user):
    Response(post_user).assert_status_code(201)