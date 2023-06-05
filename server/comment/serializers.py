from rest_framework import serializers
from .models import Comment
from user.serializers import AccountSerializer
from common.mixins import CombinedMixin

class CommentSerializer(CombinedMixin, serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    required_fields = {
        'content': 'Please enter a comment',
        'item': 'Please enter an item',
    }

    class Meta:
        model = Comment
        fields = ['id', 'item', 'content', 'owner', 'created_at', 'updated_at']
