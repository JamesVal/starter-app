from rest_framework import serializers
from .models import Item
from comment.serializers import CommentSerializer
from user.serializers import AccountSerializer
from common.mixins import CombinedMixin

class ItemSerializer(CombinedMixin, serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    owner = AccountSerializer(read_only=True)
    required_fields = {
        'itemName': 'Please enter an item name',
        'itemDescription': 'Please enter an item description',
        'type': 'Please select a type',
    }

    class Meta:
        model = Item
        fields = ['id', 'itemName', 'itemDescription', 'type', 'owner', 'comments', 'created_at', 'updated_at']
