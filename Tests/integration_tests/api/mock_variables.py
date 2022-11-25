msg_success = {"msg": "Boa Noite"}
msg_non_string = {"msg": 15}
msg_null = {"msg": None}

data_login = {
    "username": "jefecito"
}
bad_data_login = {
    "username": 42
}

key = 'Test'
value = "The message test"

value1 = "The message test 1"
value2 = "The message test 2"

URL_LOGING = "http://localhost:4000/api/login"
URL_VERIFY = 'http://localhost:4000/api/verify/token'
URL_QUEUE = 'http://localhost:4000/api/queue'

expected_response_push = {"status": "ok"}