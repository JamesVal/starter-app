from rest_framework import serializers
from .models import Item
from comment.serializers import CommentSerializer
from user.serializers import AccountSerializer

class ItemSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    owner = AccountSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['itemName', 'itemDescription', 'type', 'owner', 'comments', 'created_at', 'updated_at']
