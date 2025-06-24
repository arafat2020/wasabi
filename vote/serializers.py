from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields: dict[str] = '__all__'
        read_only_fields = ['user']
    
    def create(self, validated_data):
        vote, created = Vote.objects.update_or_create(
            user=validated_data['user'],
            post=validated_data['post'],
            defaults={'value': validated_data['value']}
        )
        return vote