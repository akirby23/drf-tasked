from rest_framework import generics, permissions
from .serializers import TaskSerializer
from .models import Task

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
