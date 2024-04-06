from drf_tasked.permissions import IsOwnerOrReadOnly, IsAssigneeOrReadOnly
from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TaskSerializer
from .models import Task

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.annotate(
        comments_count=Count(
            'comment', 
            distinct=True,
        )
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
        ] 
    ordering_fields=[
        'comments_count'
    ]
    search_fields = [ 
        'title', 
        'category__name'
    ]
    filterset_fields = [
        'owner__profile',
        'assignee',
     ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly | IsAssigneeOrReadOnly]
    queryset = Task.objects.annotate(
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')
