from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile


class ProfileTests(APITestCase):
    def test_profile_created_upon_signup(self):
        User.objects.create_user(username='jane', password='p2T9GMDF')
        user = User.objects.get(username='jane')
        profile = Profile.objects.get(owner=user)
        self.assertTrue(Profile.objects.filter(owner=user).exists())

class ProfileListTests(APITestCase):
    def test_retrieve_profile_list(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProfileDetailTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='jane', password='p2T9GMDF')
        user2 = User.objects.create_user(username='john', password='4Jp7L3Kx')
        
    def test_retrieve_profile_with_valid_id(self):
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_profile_with_invalid_id(self):
        response = self.client.get('/profiles/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_can_update_own_profile_while_logged_in(self):
        self.client.login(username='jane', password='p2T9GMDF')
        response = self.client.put('/profiles/1/', {'username': 'janie'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.username, 'janie')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_update_other_user_profile_while_logged_in(self):
        self.client.login(username='jane', password='p2T9GMDF')
        response = self.client.put('/profiles/2/', {'username': 'johnny'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_profile(self):
        response = self.client.put('/profiles/1/', {'content': 'new content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)