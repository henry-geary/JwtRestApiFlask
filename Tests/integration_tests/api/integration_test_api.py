try:
    import json
    import pytest
    import redis
    import Tests.integration_tests.api.mock_variables as mv
    import requests
    import os

except Exception as e:
    print("Some Modules are  Missing {} ".format(e))


def test_integration():
    # Get Token
    token = json.loads(requests.post(mv.URL_LOGING, json=mv.data_login).content)
    token = token["token"]

    # Verify token
    response = requests.get(mv.URL_VERIFY, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

    # Verify redis connection
    check_redis = requests.get(mv.URL_QUEUE + "/ping_redis", headers={"Authorization": f"Bearer {token}"})
    assert check_redis.content.decode("utf-8") == '{\n  "Connection": "OK"\n}\n'

    # Verify push & pop & count endpoint
    count1 = requests.get(mv.URL_QUEUE + "/count", headers={"Authorization": f"Bearer {token}"})
    assert count1.status_code == 200

    # Set currentCount with the actual redis db massage count
    currentCount = json.loads(count1.content.decode("utf-8"))["count"]

    requests.post(mv.URL_QUEUE + "/push", json=mv.msg_success, headers={"Authorization": f"Bearer {token}"})
    requests.post(mv.URL_QUEUE + "/push", json=mv.msg_success, headers={"Authorization": f"Bearer {token}"})
    pop1 = requests.get(mv.URL_QUEUE + "/pop", headers={"Authorization": f"Bearer {token}"})
    assert pop1.content.decode("utf-8") == '{\n  "message": "Boa Noite"\n}\n'

    count2 = requests.get(mv.URL_QUEUE + "/count", headers={"Authorization": f"Bearer {token}"})
    # 1 more message added to the list and one more for currentCount
    assert json.loads(count2.content.decode("utf-8"))["count"] == currentCount + 1

    requests.get(mv.URL_QUEUE + "/pop", headers={"Authorization": f"Bearer {token}"})
    count3 = requests.get(mv.URL_QUEUE + "/count", headers={"Authorization": f"Bearer {token}"})
    assert json.loads(count3.content.decode("utf-8"))["count"] == currentCount
