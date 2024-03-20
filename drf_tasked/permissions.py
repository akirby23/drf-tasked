from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Code below has been borrowed from DRF documentation: 
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


# Code borrowed from andreagrandi on GitHub
# https://gist.github.com/andreagrandi/14e07afd293fafaea770f69cf66cac14
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff