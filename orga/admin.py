from django.contrib import admin
from django.contrib.auth.models import Group 

from django.contrib.auth import get_user_model
from orga.models import Category, NewsArticle, Event


class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {'fields': ('username', 'birthdate', 'email', 'profile_picture')}),

        )
    #inlines = [AddressInline]


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Category)
admin.site.register(NewsArticle)
admin.site.register(Event)
