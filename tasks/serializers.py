from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Task
from .models import TASK_STATUS


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    is_assignee = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(
        source='owner.profile.id'
        )
    assignee_profile_id = serializers.ReadOnlyField(
        source='assignee.profile.id'
        )
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_picture.url'
        )
    category_name = serializers.ReadOnlyField(
        source='category.name'
        )
    priority_level_name = serializers.ReadOnlyField(
        source='priority_level.name'
        )
    status_name = serializers.SerializerMethodField()
    assignee_name = serializers.ReadOnlyField(source='assignee.username')
    comments_count = serializers.ReadOnlyField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_is_assignee(self, obj):
        request = self.context['request']
        return request.user == obj.assignee

    def get_status_name(self, obj):
        status_name = obj.get_status_display()
        return status_name

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'is_assignee', 'profile_id',
            'assignee_profile_id', 'profile_image', 'category',
            'category_name', 'priority_level', 'priority_level_name',
            'assignee', 'assignee_name', 'title', 'created_on', 'updated_on',
            'status', 'status_name', 'task_detail', 'comments_count',
        ]
