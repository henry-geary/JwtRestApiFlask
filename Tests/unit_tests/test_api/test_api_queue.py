import json

try:
    import pytest
    import redis
    import Tests.unit_tests.test_api.mock_variables as mv
    import requests
    import os
except Exception as e:
    print("Some Modules are  Missing {} ".format(e))


@pytest.mark.parametrize("data, status_code",
                         [(mv.data_login, 200),
                          (None, 400),
                          (mv.bad_login_input, 400),
                          (mv.bad_login_user, 404)])
def test_login(client, data, status_code, login_env):
    response = client.post("http://localhost:4000/api/login", json=data)
    assert response.status_code == status_code


def test_successfully_verify_token(client, auth):
    response = client.get("/api/verify/token", headers={"Authorization": f"Bearer {auth}"})
    assert json.loads(response.get_data().decode("utf-8"))["username"] == "jefecito"


@pytest.mark.parametrize("token, status_code",
                         [("token_fail", 401),
                          (21233, 401),
                          (None, 401),
                          (True, 401)])
def test_failure_verify_token(client, token, status_code):
    response = client.get("/api/verify/token", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status_code


@pytest.mark.parametrize("json_input, status_code, message",
                         [(mv.msg_success, 200, '{"status":"ok"}\n'),
                          (mv.msg_null, 400, '{"message":"invalid message input"}\n'),
                          (mv.msg_null, 400, '{"message":"invalid message input"}\n'),
                          (mv.msg_non_string, 400, '{"message":"invalid message input"}\n')])
def test_push(client, mocker, json_input, status_code, message, auth):
    mocker.patch("Services.queue.push_redis", return_value=1)
    response = client.post("/api/queue/push", json=json_input, headers={"Authorization": f"Bearer {auth}"})

    assert response.status_code == status_code
    assert response.get_data().decode("utf-8") == message


@pytest.mark.parametrize("size, message, message_return",
                         [(0, None, '{"message":"Queue is empty"}\n'),
                          (1, "Hi! i am a message", '{"message":"Hi! i am a message"}\n')])
def test_pop(client, mocker, size, message, message_return, auth):
    mocker.patch("Services.queue.pop_redis", return_value=message)
    mocker.patch("Services.queue.count_redis", return_value=size)

    response = client.get("/api/queue/pop", headers={"Authorization": f"Bearer {auth}"})
    assert response.get_data().decode("utf-8") == message_return


@pytest.mark.parametrize("size, status_code",
                         [(0, 200),
                          (3, 200)])
def test_count(client, mocker,size, status_code, auth):
    mocker.patch("Services.queue.count_redis", return_value=size)
    response = client.get("/api/queue/count", headers={"Authorization": f"Bearer {auth}"})
    assert response.status_code == status_code


if __name__ == "__main__":
    pytest.main()
