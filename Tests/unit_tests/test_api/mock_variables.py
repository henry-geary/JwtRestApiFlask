msg_success = {"msg": "The message test"}
msg_non_string = {"msg": 15}
msg_null = {"msg": None}

data_login = {"username": "jefecito"}
bad_login_user = {"username": "Kafka"}
bad_login_input = {"name": 321}


key = 'Test'
value = "The message test"

value1 = "The message test 1"
value2 = "The message test 2"

URL_LOGING_TEST = "http://localhost:8000/api/login"
URL_TOKEN_TEST = 'http://localhost:8000/api/verify/token'
URL_QUEUE = 'http://localhost:8000/queue/'

expected_response_push = {"status": "ok"}