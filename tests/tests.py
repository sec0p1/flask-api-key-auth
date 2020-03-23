"""Test script."""

import unittest
import requests


class BookTests(unittest.TestCase):
    """Books tests class."""

    url = 'http://127.0.0.1:5000/api/'

    def test_get_books_unauthorized(self):
        """Test if unathorized request will fail."""
        response = requests.get(self.url + 'books')
        self.assertEqual(401, response.status_code)

    def test_get_books_authorized(self):
        """Test if athorized request will succeed."""
        headers = {'Authorization': 'abcdef12345'}
        response = requests.get(self.url + 'books', headers=headers)
        self.assertEqual(200, response.status_code)

    def test_get_books_authorized_wrong_key(self):
        """Test if athorized request with wrong key will fail."""
        headers = {'Authorization': 'wrong_api_key'}
        response = requests.get(self.url + 'books', headers=headers)
        self.assertEqual(401, response.status_code)


if __name__ == '__main__':
    unittest.main()
