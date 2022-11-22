try:
    from app.__main__ import app
    import unittest
    import requests
    from os import getenv
    from dotenv import load_dotenv
    import json
    from redis import Redis




except Exception as e:
    print("Some modules are Missing {} ".format(e))


class FlaskTest(unittest.TestCase):
    r = Redis(host="redis-container", port=6379)
    load_dotenv()
    dataAdmin = {'username': getenv("ADMIN")}
    dataPush = {"msg": "15"}
    currentCount = r.llen("Queue")

    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api/ping")
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    # Check for the content response
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/api/ping")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    # Check for the data response
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/api/ping")
        self.assertEqual(b'pong', response.data)

    # Check for ping redis
    def test_ping_redis(self):
        response = requests.get("http://127.0.0.1:4000/api/queue/ping_redis",
                                headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), '{\n  "Connection": "OK"\n}\n')

    # Check JWT token all OK
    def test_validate_token(self):
        response = requests.get("http://localhost:4000/api/verify/token", json=self.dataAdmin,
                                headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 200)

    # Check JWT token invalid data input
    def test_login_error(self):
        response = requests.post("http://localhost:4000/api/login", json={'username': 154})
        self.assertEqual(400, response.status_code)
        self.assertEqual(response.content.decode("utf-8"), '{\n  "message": "Invalid user data"\n}\n')

    # Create JWT Token
    def jwt_login(self):
        response = requests.post("http://localhost:4000/api/login", json=self.dataAdmin)
        parsed = json.loads(response.content)
        return "Bearer " + parsed["token"]

    # Check for the request data
    def test_push_error_input(self):
        response = requests.post("http://127.0.0.1:4000/api/queue/push", json={"anything": 321},
                                 headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'message': 'invalid message input'})

    # Check for successfully message added
    def test_push_output(self):
        response = requests.post("http://127.0.0.1:4000/api/queue/push", json=self.dataPush,
                                 headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'status': 'ok'})
        requests.get("http://127.0.0.1:4000/api/queue/pop",
                     headers={"Authorization": self.jwt_login()})

    # Check pop endpoint
    def test_pop_output(self):
        requests.post("http://127.0.0.1:4000/api/queue/push", json=self.dataPush,
                      headers={"Authorization": self.jwt_login()})

        response = requests.get("http://127.0.0.1:4000/api/queue/pop",
                                headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': '15'})

    def test_count_output0(self):
        response = requests.get("http://127.0.0.1:4000/api/queue/count",
                                headers={"Authorization": self.jwt_login()})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'status': 'ok', "count": self.currentCount})

    def test_count_output1(self):
        requests.post("http://127.0.0.1:4000/api/queue/push", json=self.dataPush,
                      headers={"Authorization": self.jwt_login()})

        response = requests.get("http://127.0.0.1:4000/api/queue/count",
                                headers={"Authorization": self.jwt_login()})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'status': 'ok', "count": self.currentCount + 1})

        requests.get("http://127.0.0.1:4000/api/queue/pop",
                     headers={"Authorization": self.jwt_login()})


if __name__ == "__main__":
    unittest.main()
