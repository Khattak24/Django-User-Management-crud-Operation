from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from user_module.serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from user_module.models import Article

# Create your views here.
class ListArticleAPIView(ListAPIView):
    """List all of the available Articles from the database"""
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer

class CreateArticleAPIView(CreateAPIView):
    """Allows for creation of a Article"""
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer

class UpdateArticleAPIView(UpdateAPIView):
    """Allows for updating a specific Article by passing in the id of the Article to update"""
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer

class DeleteArticleAPIView(DestroyAPIView):
    """Allows for deletion of a specific Article from the database"""
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer