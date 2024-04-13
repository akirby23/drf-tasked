from rest_framework import generics, filters
from drf_tasked.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer


# The models below have been adapted from Code Institute's drf-api walkthrough
class ProfileList(generics.ListAPIView):
    """
    Retrieves and lists all profiles
    """
    queryset = Profile.objects.annotate(
        created_tasks_count=Count(
            'owner__task',
            distinct=True
            )
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    ordering_fields = [
        'created_tasks_count',
    ]
    filterset_fields = [
        'owner__profile',
     ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Read or update a profile if you're the owner
    Displays tasks count
    """
    queryset = Profile.objects.annotate(
        created_tasks_count=Count(
            'owner__task',
            distinct=True
            )
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
