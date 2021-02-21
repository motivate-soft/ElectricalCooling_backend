from djoser.conf import settings
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "first_name",
            "last_name",
        )
