from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class RegisterViewSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['avatar', 'username', 'nickname', 'password']

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'access': user.token()['access'],
            'refresh': user.token()['refresh'],
        }

    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        user = authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')

        return {
            'username': user.username,
            'tokens': user.token()
        }