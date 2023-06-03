from django.db.models import Prefetch
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from common.permissions import CommonPermission
from comment.models import Comment

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [CommonPermission]

    def get_queryset(self):
        prefetch_related_models = Prefetch('comments', queryset=Comment.objects.order_by('-created_at'))
        queryset = Item.objects.prefetch_related(prefetch_related_models)
        return queryset