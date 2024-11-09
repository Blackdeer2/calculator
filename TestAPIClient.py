import unittest
from unittest.mock import patch
from APIClient import APIClient

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "title": "Test Post"}]

        result = self.client.get_data("posts")
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["title"], "Test Post")

    @patch('requests.get')
    def test_get_data_by_id_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "title": "Test Post"}

        result = self.client.get_data_by_id("posts", 1)
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["title"], "Test Post")

    @patch('requests.get')
    def test_get_all_users_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "name": "Leanne Graham"}]

        result = self.client.get_all_users()
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "Leanne Graham")

    @patch('requests.get')
    def test_get_user_by_id_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "name": "Leanne Graham"}

        result = self.client.get_user_by_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "Leanne Graham")

    @patch('requests.get')
    def test_get_all_comments_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "postId": 1, "userId": 1, "comment": "Sample comment"}]

        result = self.client.get_all_comments()
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["postId"], 1)
        self.assertEqual(result[0]["comment"], "Sample comment")

    @patch('requests.get')
    def test_get_comment_by_id_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "postId": 1, "userId": 1, "comment": "Sample comment"}

        result = self.client.get_comment_by_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["postId"], 1)
        self.assertEqual(result["comment"], "Sample comment")

if __name__ == "__main__":
    unittest.main()
