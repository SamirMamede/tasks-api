from rest_framework import serializers
from tasks.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')