from rest_framework import serializers
from core.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read']
        read_only_fields = ['id']
