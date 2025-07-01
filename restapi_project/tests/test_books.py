import unittest
from app import app

class BooksTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_ping(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)
        # Bug: ping does not return JSON so this fails

if __name__ == '__main__':
    unittest.main()