import requests
import sys


class BaseClient:
    username = ""

    def __init__(self, username):
        self.username = username

    # URL vk api
    BASE_URL = "https://api.vk.com/method/"
    # метод vk api
    method = ""

    # Получение GET параметров запроса
    def get_params(self):
        return None

    # Склейка url
    def generate_url(self, method):
        url = '{0}{1}'.format(self.BASE_URL, method)
        return url

    # Отправка запроса к VK API
    def _get_data(self, method):
        response = None
        try:
            response = requests.get(self.generate_url(self.method), params=self.get_params())
        except requests.RequestException as re:
            print("Ошибка при выполнении запроса ", re)
            sys.exit(-1)
        if response is None:
            print("Пустой ответ")
            sys.exit(-1)
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        print(response.text)
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(self.method)
