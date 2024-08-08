from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_street_address1', 'default_town_or_city', 'default_country')

# Ensure this is the only registration
admin.site.register(UserProfile, UserProfileAdmin)
