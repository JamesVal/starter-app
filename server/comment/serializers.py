from rest_framework import serializers
from .models import Comment
from user.serializers import AccountSerializer

class CommentSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'owner', 'created_at', 'updated_at']
