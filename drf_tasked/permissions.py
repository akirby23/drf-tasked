from rest_framework import permissions

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
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to edit an object.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAssigneeOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow assignees of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the assignee of the snippet.
        return obj.assignee == request.user