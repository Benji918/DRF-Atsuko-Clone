from rest_framework import serializers
from core.models import MerchantProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantProfile
        fields = ['id', 'merchant_name', 'description']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantProfile
        fields = ['id', 'profile_image']
        read_only_fields = ['id', 'created_at', 'updated_at']