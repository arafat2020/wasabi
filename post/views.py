from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  
    
    @action(detail=False, methods=['get'], url_path='my', permission_classes=[permissions.IsAuthenticated])
    def my_posts(self, request):
        posts = Post.objects.filter(user=request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)