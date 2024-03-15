from rest_framework import generics
from drf_tasked.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# The models below have been adapted from Code Institute's drf-api walkthrough

class ProfileList(generics.ListAPIView):
    """
    Retrieves and lists all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Read or update a profile if you're the owner
    Read task details to be added later
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

