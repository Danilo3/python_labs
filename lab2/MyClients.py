from BaseClient import BaseClient
from datetime import datetime
import re
import sys


class UserIdClient(BaseClient):

    def __init__(self, username):
        super().__init__(username)

    method = "users.get"

    def response_handler(self, response):
        response_json = response.json()
        uid = 0
        try:
            uid = response_json.get("response")[0].get("uid")
        except (KeyError, TypeError, IndexError):
            print("No such user")
            sys.exit(-1)
        if uid == 0:
            print("Значение id не было получено")
            sys.exit(-1)
        return uid

    def get_params(self):
        return {"user_ids": self.username}


class FriendsBirthdaysClient(BaseClient):

    method = "friends.get"

    def __init__(self, uid):
        super().__init__(uid)

    def response_handler(self, response):
        response_json = response.json()
        return self.get_ages(response_json)

    def get_params(self):
        return {"user_id": self.username, "fields": "bdate"}

    @staticmethod
    def get_ages(response_json):
        ages = []
        today = datetime.today ()
        pattern = re.compile("^\d{1,2}\.\d{1,2}\.\d{4}$")
        try:
            users = response_json.get("response", [])
            for user in users:
                birthday_date = user.get("bdate")
                if birthday_date:
                    if pattern.search(birthday_date):
                        date = datetime.strptime(birthday_date, "%d.%m.%Y")
                        ages.append(int(round((today - date).days / 365, 0)))
        except (KeyError, TypeError):
            print("Incorrect json response")
        if len(ages) == 0:
            print("Нет данных о днях рождения")
            sys.exit(-1)
        return ages
