from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import PriorityLevel

class PriorityLevelListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='q5vwm5pv')
        User.objects.create_user(username='user', password='1mn6ah5d')

    def test_superuser_can_create_priority_level(self):
        self.client.login(username='admin', password='q5vwm5pv')
        response = self.client.post('/priority-levels/', {'name': 'Low', 'description':'Low'})
        count = PriorityLevel.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_superuser_cannot_create_priority_level(self):
        self.client.login(username='user', password='1mn6ah5d')
        response = self.client.post('/priority-levels/', {'name': 'Low', 'description':'Low'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_retrieve_priority_level_list(self):
        response = self.client.get('/priority-levels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PriorityLevelDetailViewTests(APITestCase):
    def setUp(self):
        admin = User.objects.create_superuser(username='admin', password='q5vwm5pv')
        user = User.objects.create_user(username='user', password='1mn6ah5d')
        prioritylevel1 = PriorityLevel.objects.create(name="Low", description="Low")
        prioritylevel2 = PriorityLevel.objects.create(name="High", description="High")

    def test_can_retrieve_priority_level_with_valid_id(self):
        response = self.client.get('/priority-levels/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_priority_level_with_invalid_id(self):
        response = self.client.get('/priority-levels/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_superuser_can_update_priority_level(self):
        self.client.login(username='admin', password='q5vwm5pv')
        response = self.client.put('/priority-levels/1/', {'name': 'Medium', 'description': 'Medium'})
        prioritylevel = PriorityLevel.objects.filter(pk=1).first()
        self.assertEqual(prioritylevel.name, 'Medium')
        self.assertEqual(prioritylevel.description, 'Medium')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_superuser_cannot_update_priority_level(self):
        self.client.login(username='user', password='1mn6ah5d')
        response = self.client.put('/priority-levels/1/', {'name':'Edited priority level'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)