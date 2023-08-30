from django.contrib.auth.models import Group 
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

from .models import NewsArticle, Category, Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ["url","username","email","groups","birthdate"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group 
        fields = ["url", "name"]



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = NewsArticle
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'