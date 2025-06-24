from rest_framework import viewsets, permissions
from .models import Vote
from rest_framework.response import Response
from rest_framework import status
from .serializers import VoteSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)