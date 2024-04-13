from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task
from categories.models import Category
from prioritylevels.models import PriorityLevel


class TaskListViewTests(APITestCase):
    """
    Tests task list view endpoints
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='aoife', password='vGTdHgV2'
            )
        self.category = Category.objects.create(
            name='Social'
            )
        self.priority_level = PriorityLevel.objects.create(
            name='Low'
            )

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
    """
    Tests task detail view endpoints
    """
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='aoife', password='vGTdHgV2'
            )
        self.user2 = User.objects.create_user(
            username='aoife2', password='5htgwhxe'
            )
        self.user3 = User.objects.create_user(
            username='aoife3', password='4htgwhLe'
            )
        self.category1 = Category.objects.create(
            name='Work'
            )
        self.category2 = Category.objects.create(
            name='Education'
            )
        self.priority_level1 = PriorityLevel.objects.create(
            name='Low'
            )
        self.priority_level2 = PriorityLevel.objects.create(
            name='High'
            )
        self.task1 = Task.objects.create(
            owner=self.user1,
            title='Test task 1',
            category=self.category1,
            priority_level=self.priority_level1,
            task_detail='Test task 1',
            assignee=self.user2,
            status='IN_PROGRESS'
            )
        task2 = Task.objects.create(
            owner=self.user2,
            title='Test task 2',
            category=self.category2,
            priority_level=self.priority_level2,
            task_detail='Test task 2',
            assignee=self.user2,
            status='IN_PROGRESS'
            )

    def test_can_retrieve_task_with_valid_id(self):
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_task_with_invalid_id(self):
        response = self.client.get('/tasks/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_own_task_while_logged_in(self):
        self.client.login(username='aoife', password='vGTdHgV2')
        response = self.client.put('/tasks/1/', {
            'title': 'A different title',
            'category': self.category1.id,
            'priority_level': self.priority_level1.id,
            'task_detail': 'Test task 1',
            'assignee': self.user2.id,
            'status': 'IN_PROGRESS'
            })
        task = Task.objects.filter(pk=1).first()
        self.assertEqual(task.title, 'A different title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_assignee_can_update_task(self):
        self.client.login(username='aoife2', password='5htgwhxe')
        response = self.client.put('/tasks/1/', {
            'title': 'A different title',
            'category': self.category1.id,
            'priority_level': self.priority_level1.id,
            'task_detail': 'Test task 1',
            'assignee': self.user2.id,
            'status': 'IN_PROGRESS'
            })
        task = Task.objects.filter(pk=1).first()
        self.assertEqual(task.title, 'A different title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_assignee_non_owner_cannot_update_task(self):
        self.client.login(username='aoife3', password='4htgwhLe')
        response = self.client.put('/tasks/1/', {
            'title': 'Test task 1',
            'category': self.category1.id,
            'priority_level': self.priority_level1.id,
            'task_detail': 'Edited task details',
            'assignee': self.user2.id,
            'status': 'IN_PROGRESS'
            })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_update_other_user_task_while_logged_in(self):
        self.client.login(username='aoife', password='vGTdHgV2')
        response = self.client.put(
            '/tasks/2/',
            {'title': 'A different title'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_task(self):
        response = self.client.put(
            '/tasks/1/',
            {'title': 'A different title'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
