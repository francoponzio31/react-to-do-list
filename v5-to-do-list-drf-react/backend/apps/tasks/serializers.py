from rest_framework import serializers


class TaskBodySerializer(serializers.Serializer):
    text = serializers.CharField()
    done = serializers.BooleanField(required=False)


class TaskOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    done = serializers.BooleanField()
    user_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
