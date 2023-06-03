from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.owner.user == request.user) or request.user.is_superuser

class CommonPermission(permissions.BasePermission):
    def get_permissions(self, action):
        if action == 'list':
            permission_classes = [AllowAny]
        elif action == 'retrieve':
            permission_classes = [AllowAny]
        elif action == 'create':
            permission_classes = [IsAuthenticated]
        elif action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerPermission]
        else:
            permission_classes = [IsAuthenticated]

        return permission_classes

    def has_permission(self, request, view):
        permission_classes = self.get_permissions(view.action)
        return all(
            permission().has_permission(request, view)
            for permission in permission_classes
        )

    def has_object_permission(self, request, view, obj):
        permission_classes = self.get_permissions(view.action)
        return all(
            permission().has_object_permission(request, view, obj)
            for permission in permission_classes
        )
