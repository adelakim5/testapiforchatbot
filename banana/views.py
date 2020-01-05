from django.shortcuts import render
from rest_framework import viewsets
from .models import Post

## Serializers
from .serializers import PostSerializer

# Create your views he`re.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer