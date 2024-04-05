from rest_framework import serializers
from .models import Profile

# Code below has been adapted from Code Institute's drf-api walkthrough project

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_tasks_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        """
        Throws a value error if the profile picture 
        is larger than 2MB, or more than 1080px in 
        height/width
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Profile picture size larger than 2MB!'
            )
        if value.image.width > 1080:
            raise serializers.ValidationError(
                'Profile picture width larger than 1080px!'
            )
        if value.image.height > 1080:
            raise serializers.ValidationError(
                'Profile picture height larger than 1080px!'
            )
        return value

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'username', 'created_on', 'updated_on', 'content',
            'profile_picture', 'created_tasks_count', 'assigned_tasks_count',
        ]