from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be read in responses
