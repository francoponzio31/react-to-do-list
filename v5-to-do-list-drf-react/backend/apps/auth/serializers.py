from rest_framework import serializers


class LoginBodySerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class SignupBodySerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    creation_date = serializers.DateTimeField()