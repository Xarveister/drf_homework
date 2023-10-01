from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """Generic-класс для обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
