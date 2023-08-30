from django.contrib.auth.models import Group 
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets
from rest_framework import permissions
from orga.serializers import UserSerializer, GroupSerializer, NewsArticleSerializer, CategorySerializer, EventSerializer
from orga.models import Category, NewsArticle, Event

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer