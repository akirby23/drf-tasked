from drf_tasked.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CommentSerializer
from .models import Comment


class CommentList(generics.ListCreateAPIView):
    """
    Lists all comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['task']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Displays individual comment details
    Allows comments to be retrieved, updated
    or destroyed
    """
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
