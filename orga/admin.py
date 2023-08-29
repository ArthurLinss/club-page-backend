from django.contrib import admin

from .models import User



class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {'fields': ('username', 'birthdate', 'email', 'profile_picture')}),

        )
    #inlines = [AddressInline]


admin.site.register(User, UserAdmin)
