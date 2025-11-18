from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from items.models import Item

class ItemAPITest(TestCase):
    # load test fixtures before test runs
    fixtures = ['items.json']   

    def setUp(self):
        self.client = APIClient()

    def test_list_items(self):
        url = reverse('item-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_item(self):
        url = reverse('item-list')
        data = {
            "name": "MacBook M4 Pro",
            "description": "48GB RAM with 1TB SSD powerful machine",
            "price": "13000000"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.count(), 3)
