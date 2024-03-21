from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Category

class CategoryListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='q5vwm5pv')
        User.objects.create_user(username='user', password='1mn6ah5d')

    def test_superuser_can_create_category(self):
        self.client.login(username='admin', password='q5vwm5pv')
        response = self.client.post('/categories/', {'name': 'Social', 'description':'Social'})
        count = Category.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_superuser_cannot_create_category(self):
        self.client.login(username='user', password='1mn6ah5d')
        response = self.client.post('/categories/', {'name': 'Social', 'description':'Social'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_retrieve_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CategoryDetailViewTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_superuser(username='admin', password='q5vwm5pv')
        user = User.objects.create_user(username='user', password='1mn6ah5d')
        category1 = Category.objects.create(name="Work", description="Work")
        category2 = Category.objects.create(name="Education", description="Education")

    def test_can_retrieve_category_with_valid_id(self):
        response = self.client.get('/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_category_with_invalid_id(self):
        response = self.client.get('/categories/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_can_update_category(self):
        self.client.login(username='admin', password='q5vwm5pv')
        response = self.client.put('/categories/1/', {'description': 'Edited category'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_superuser_cannot_update_category(self):
        self.client.login(username='user', password='1mn6ah5d')
        response = self.client.put('/categories/1/', {'name':'Edited category'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)