from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task
from categories.models import Category
from prioritylevels.models import PriorityLevel

class TaskListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='aoife', password='vGTdHgV2')
        self.category = Category.objects.create(name='Social')
        self.priority_level = PriorityLevel.objects.create(name='Low')

    def test_logged_in_user_can_create_a_task(self):
        self.client.login(username='aoife', password='vGTdHgV2')
        response = self.client.post(
            '/tasks/', 
            {
            'owner': self.user.id,
            'title': 'A title',
            'category': self.category.id,
            'priority_level': self.priority_level.id,
            'task_detail': 'Test task',
            'assignee': self.user.id,
            'status': 'IN_PROGRESS'
            })
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve_task_list(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskDetailViewTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='aoife', password='vGTdHgV2')
        user2 = User.objects.create_user(username='aoife2', password='5htgwhxe')
        user3 = User.objects.create_user(username='aoife3', password='4htgwhLe')
        category1 = Category.objects.create(name='Work')
        category2 = Category.objects.create(name='Education')
        priority_level1 = PriorityLevel.objects.create(name='Low')
        priority_level2 = PriorityLevel.objects.create(name='High')
        task1 = Task.objects.create(
            owner= user1, 
            title='Test task 1', 
            category=category1,
            priority_level=priority_level1,
            task_detail='Test task 1',
            assignee=user2,
            status='IN_PROGRESS'
            )
        task2 = Task.objects.create(
            owner= user2, 
            title='Test task 2', 
            category=category2,
            priority_level=priority_level2,
            task_detail='Test task 2',
            assignee=user2,
            status='IN_PROGRESS'
            )

    def test_can_retrieve_task_with_valid_id(self):
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_task_with_invalid_id(self):
        response = self.client.get('/tasks/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_can_update_own_task_while_logged_in(self):
    #     self.client.login(username='aoife', password='vGTdHgV2')
    #     response = self.client.put('/tasks/1/', {'title': 'A different title'})
    #     # task = Task.objects.filter(pk=1).first()
    #     # self.assertEqual(task.title, 'A different title')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_assignee_can_update_task(self):
    #     self.client.login(username='aoife2', password='5htgwhxe')
    #     response = self.client.put('/tasks/1/', {'title': 'A different title'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_non_assignee_non_owner_cannot_update_task(self):
    #     self.client.login(username='aoife2', password='5htgwhxe')
    #     response = self.client.put('/tasks/1/', {'task_detail': 'Edited task'})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cannot_update_other_user_task_while_logged_in(self):
        self.client.login(username='aoife', password='vGTdHgV2')
        response = self.client.put('/tasks/2/', {'title': 'A different title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_task(self):
        response = self.client.put('/tasks/1/', {'title': 'A different title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
