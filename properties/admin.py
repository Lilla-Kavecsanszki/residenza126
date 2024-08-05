from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'property_type', 'price', 'bedrooms', 'bathrooms', 'created_at')
    list_filter = ('property_type', 'location', 'created_at')
    search_fields = ('name', 'description', 'location', 'property_type', 'features')
    list_editable = ('price',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'location', 'property_type', 'features')
        }),
        ('Media', {
            'fields': ('video_url', 'image_url')
        }),
        ('Details', {
            'fields': ('bedrooms', 'bathrooms', 'price', 'size')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
