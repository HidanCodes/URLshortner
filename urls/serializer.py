from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Urls


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = ['url', 'number']


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
