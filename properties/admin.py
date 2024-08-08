from django.contrib import admin
from .models import Property
from .forms import PropertyForm

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm
    list_display = ('name', 'price', 'size', 'bedrooms', 'bathrooms')
