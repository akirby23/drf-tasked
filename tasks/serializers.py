from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_picture.url')
    category_name = serializers.ReadOnlyField(source='category.name')
    priority_level_name = serializers.ReadOnlyField(source='priority_level.name')
    assignee_name = serializers.ReadOnlyField(source='assignee.username')
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
            model = Task
            fields = [
                'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'category_name', 
                'priority_level_name', 'assignee_name', 'title', 'created_on', 'updated_on', 'category', 
                'priority_level', 'status', 'task_detail', 'assignee', 'comments_count',
            ]
