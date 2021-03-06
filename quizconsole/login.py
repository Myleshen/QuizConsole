import requests

class Login:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.jwtToken = ""

    def login(self):
        response = requests.post(url="http://localhost:8080/authenticate",
                                json={
                                    "userName":self.userName,
                                    "password":self.password
                                    }
                                )
        self.jwtToken = response.json()["jwtToken"]
