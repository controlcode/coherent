import unittest

from coherent.application import app

class TestLogin(unittest.TestCase):
    """Test case for login view"""

    def setUp(self):
        self.app = app.test_client()

    def test_view_login(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)