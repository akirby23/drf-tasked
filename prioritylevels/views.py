from rest_framework import generics
from .serializers import PriorityLevelSerializer
from .models import PriorityLevel

class PriorityLevelList(generics.ListCreateAPIView):
    serializer_class = PriorityLevelSerializer
    queryset = PriorityLevel.objects.all()



