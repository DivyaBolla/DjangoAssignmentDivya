from rest_framework import serializers
from . models import User

# class UserSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     phone = serializers.IntegerField()
#     email = serializers.EmailField()


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id', 'name', 'email', 'phone']
        