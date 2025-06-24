from django.db import models
from post.models import Post
from django.contrib.auth.models import User

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    value = models.BooleanField()
    