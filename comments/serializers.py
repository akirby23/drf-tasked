from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Adapted from Code Institutes's drf_api walkthrough project
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username'
        )
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(
        source='owner.profile.id'
        )
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_picture.url'
        )
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'task', 'created_on', 'updated_on', 'comment_detail'
        ]


class CommentDetailSerializer(CommentSerializer):
    task = serializers.ReadOnlyField(source='task.id')
