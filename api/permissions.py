from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or (
                obj.owner == request.user):
            return True

        raise PermissionDenied({
            "detail": "Отстаньте от чужого кота )"
        })
