from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):

    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='articles',blank=True)
    is_public = models.BooleanField(default=True)  # New field for public/private

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    attendees = models.ManyToManyField(User, related_name='events_attending', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title