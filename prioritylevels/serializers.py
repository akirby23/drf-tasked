from rest_framework import serializers
from .models import PriorityLevel


class PriorityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityLevel
        fields = [
            'id', 'name', 'description',
        ]
