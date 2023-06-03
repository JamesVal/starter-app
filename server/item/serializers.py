from rest_framework import serializers
from .models import Item
from comment.serializers import CommentSerializer

class ItemSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
