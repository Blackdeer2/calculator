import requests
from requests.exceptions import RequestException

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        pass

    def get_data(self, endpoint):
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні даних з {endpoint}: {e}")
            return None

    def get_data_by_id(self, endpoint, item_id):
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}/{item_id}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні даних з {endpoint} за ID {item_id}: {e}")
            return None

    def get_all_users(self):
        try:
            response = requests.get(f"{self.BASE_URL}/users")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні всіх користувачів: {e}")
            return None

    def get_user_by_id(self, user_id):
        try:
            response = requests.get(f"{self.BASE_URL}/users/{user_id}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні користувача з ID {user_id}: {e}")
            return None

    def get_all_comments(self):
        try:
            response = requests.get(f"{self.BASE_URL}/comments")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні всіх коментарів: {e}")
            return None

    def get_comment_by_id(self, comment_id):
        try:
            response = requests.get(f"{self.BASE_URL}/comments/{comment_id}")
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"Помилка при отриманні коментаря з ID {comment_id}: {e}")
            return None