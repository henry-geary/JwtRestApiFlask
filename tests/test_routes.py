try:
    import pytest
    import tests.mock_variables as mv
    import requests
    import json

except Exception as e:
    print("Some Modules are  Missing {} ".format(e))


@pytest.mark.parametrize("req_json, status_code",
                         [(mv.req_push_OK, 200),
                          (mv.req_push_BAD1, 400),
                          (mv.req_push_BAD2, 404)])
def test_push(client, mocker, req_json, status_code, app):

    mocker.patch("function_jwt.validate_token", return_value=True)

    token = login_jwt(client)

    response = client.post(mv.url_queue + "/post", json=req_json, headers={"Authorization": token})
    print(response)
    assert response.status_code == status_code


def login_jwt(client):
    response = client.post("http://localhost:4000/api/login", json=mv.req_login_OK)
    parsed = json.loads(response.get_data())

    return "Bearer " + parsed["token"]
