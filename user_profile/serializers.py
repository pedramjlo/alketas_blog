from rest_framework import serializers

from .models import Avatar, Profile


class AvatarChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ('image',)



class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'role',)