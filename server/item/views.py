from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from common.permissions import IsOwnerPermission

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerPermission]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
