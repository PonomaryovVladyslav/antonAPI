from rest_framework import permissions


class CreateOnlyByAdmin(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
