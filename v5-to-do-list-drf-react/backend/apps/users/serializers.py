from rest_framework import serializers


class UserBodySerializer(serializers.Serializer):
    username = serializers.CharField()


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    creation_date = serializers.DateTimeField()
