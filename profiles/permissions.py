from rest_framework import permissions

class IsOwnerOrMerchant(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or merchants to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow editing if the user is the owner of the object or a merchant
        return obj.user == request.user or request.user.is_merchant