from rest_framework import generics
from drf_tasked.permissions import IsAdminOrReadOnly
from .serializers import PriorityLevelSerializer
from .models import PriorityLevel

class PriorityLevelList(generics.ListCreateAPIView):
    serializer_class = PriorityLevelSerializer
    queryset = PriorityLevel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class PriorityLevelDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PriorityLevelSerializer
    queryset = PriorityLevel.objects.all()
    permission_classes = [IsAdminOrReadOnly]

