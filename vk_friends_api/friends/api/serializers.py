from rest_framework import serializers
from .models import User, FriendRequest, FriendsPair


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['user1_id', 'user2_id']


class FriendsPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsPair
        fields = ['user1_id', 'user2_id']