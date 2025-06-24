from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']
    
    def create(self, validated_data):
        comment, created = Comment.objects.update_or_create(
            user=validated_data['user'],
            post=validated_data['post'],
            defaults={'content': validated_data['content']}
        )
        return comment