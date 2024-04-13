from rest_framework import generics
from drf_tasked.permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer
from .models import Category


class CategoryList(generics.ListCreateAPIView):
    """
    Lists all categories
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Displays individual category details
    Can be retrieved, updated or destroyed
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly]
