from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    up_votes = serializers.SerializerMethodField()
    down_votes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user', 'up_votes', 'down_votes']
        read_only_fields = ['user']
    
    def get_up_votes(self, obj) -> int:
        return obj.votes.filter(value=True).count()

    def get_down_votes(self, obj) -> int:
        return obj.votes.filter(value=False).count()