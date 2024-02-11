from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import KZ_dashboard, Category
import json


class APITestCase(TestCase):
    def test_unauthenticated_access(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertIn('/signin', response.url)

    def test_authenticated_access(self):
        self.client.login(username='test', password='test!')
        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def setUp(self):
        self.client = APIClient()
        self.dashboard_item = KZ_dashboard.objects.create(category=Category.objects.create(name="test caregory"),sku="test sku",name='Test Item', stock_status=100, available_stock=50)

    def test_get_dashboard_items(self):
        response = self.client.get('/dashboard/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.content), 1)


    def test_filter_dashboard_items(self):
        response = self.client.get('/dashboard/?stock_status=0&filter_type=above', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_filter_type(self):
        response = self.client.get('/dashboard/?stock_status=100&filter_type=invalid', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access_to_api(self):
        response = self.client.get('/dashboard-api/')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertIn('/login', response.url)

    def test_api_documentation_access(self):
        response = self.client.get('/api-docs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




