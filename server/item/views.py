from django.db.models import Prefetch
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from common.permissions import CommonPermission
from comment.models import Comment
from user.models import Account

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.prefetch_related(
      Prefetch('owner', queryset=Account.objects.all()),
      Prefetch('comments', queryset=Comment.objects.order_by('-created_at')),
      Prefetch('comments__owner', queryset=Account.objects.all()),
    )
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [CommonPermission]
