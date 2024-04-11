from rest_framework import viewsets, mixins, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Merchant
# from .serializers import MerchantCreateSerializer

# # Create your views here.
# class MerchantViewSets(viewsets.ModelViewSet):
#     queryset = Merchant.objects.all()
#     serializer_class = MerchantCreateSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated,]

#     def get_queryset(self):
#         """Return only merchant objects for the request user"""
#         return self.queryset.filter(user=self.request.user).order_by('-id')

#     def get_serializer_class(self):
#         return self.serializer_class