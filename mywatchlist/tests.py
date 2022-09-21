from django.test import TestCase, Client
from django.urls import resolve

class mywatchlist_test(TestCase):
    def test_url_is_exist_html(self):
        response = Client().get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)
    def test_url_is_exist_xml(self):
        response = Client().get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
    def test_url_is_exist_json(self):
        response = Client().get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)




