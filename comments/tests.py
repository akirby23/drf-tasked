from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Comment
from tasks.models import Task
from categories.models import Category
from prioritylevels.models import PriorityLevel

class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='marie', password='vrjjsz5z')
             
    # def test_logged_in_user_can_create_a_comment(self):
    #     self.client.login(username='marie', password='vrjjsz5z')
    #     response = self.client.post('/comments/', {'comment_detail': 'Test comment'})
    #     # count = Comment.objects.count()
    #     # self.assertEqual(count, 1)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_retrieve_comment_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentDetailViewTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='marie', password='vrjjsz5z')
        user2 = User.objects.create_user(username='marie2', password='vuf6eo99')
        category = Category.objects.create(name='Social')
        priority_level = PriorityLevel.objects.create(name='Low')
        task = Task.objects.create(
            owner= user1, 
            title='Test task', 
            category=category,
            priority_level=priority_level,
            task_detail='Test task',
            assignee=user2,
            status='IN_PROGRESS'
            )
        comment1 = Comment.objects.create(
            owner=user1,
            task=task,
            comment_detail="Test comment 1"
            )
        comment2 = Comment.objects.create(
            owner=user2,
            task=task,
            comment_detail="Test comment 2"
            )

    def test_can_retrieve_comment_with_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_comment_with_invalid_id(self):
        response = self.client.get('/comments/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # def test_can_update_own_comment_while_logged_in(self):
    #     self.client.login(username='marie', password='vrjjsz5z')
    #     response = self.client.put('/comments/1/', {'comment_detail': 'Comment edited'})
    #     comment = Comment.objects.filter(pk=1).first()
    #     self.assertEqual(comment.comment_detail, 'Comment edited')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cannot_update_other_user_comment_while_logged_in(self):
        self.client.login(username='aoife', password='vGTdHgV2')
        response = self.client.put('/comments/2/', {'comment_detail': 'Comment edited'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_comment(self):
        response = self.client.put('/comments/1/', {'comment_detail': 'Comment edited'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
