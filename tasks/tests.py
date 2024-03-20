from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='jane', password='p2T9GMDF')
    
    # def test_retrieve_task_list(self):
    #     jane = User.objects.get(username='jane')
    #     Task.objects.create(
    #         owner=jane, 
    #         title='A title',
    #         category='Social', 
    #         priority_level='Low',
    #         task_detail='Task details',
    #         assignee='jane')
    #     response = self.client.get('/posts/')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# class TaskDetailViewTests(APITestCase):
