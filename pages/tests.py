
from django.test import TestCase

class SimpleTestCas(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status_code(self):
        reponse = self.client.get('/about/')
        self.assertEqual(reponse.status_code, 200)

