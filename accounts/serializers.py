from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User
from django_typomatic import ts_interface, generate_ts


@ts_interface()
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["subscription"]


@ts_interface()
class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False)

    class Meta:
        model = User
        fields = [field.name for field in model._meta.fields]
        fields.remove("password")
        fields.append("user_profile")


generate_ts("./generated-types/accounts.ts")
