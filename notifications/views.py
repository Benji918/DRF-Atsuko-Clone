from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Notification
from .serializers import NotificationSerializer


class NotificationViewSets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only lodge objects for the request user"""
        return self.queryset.filter(recipient=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(recipient=self.request.user)
