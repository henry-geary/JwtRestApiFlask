import routes.redis_endpoint

try:
    import pytest
    import tests.mock_variables as mv
    import requests
    import json

except Exception as e:
    print("Some Modules are  Missing {} ".format(e))

def test_push_redis():
    data = {"msg": "hola"}
    result = routes.redis_endpoint.push_redis(data)
    assert result.status_code == 200

