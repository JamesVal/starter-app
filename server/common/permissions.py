from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.owner.user == request.user) or request.user.is_superuser
