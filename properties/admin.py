from django.contrib import admin
from .models import Property, PropertyImage, PropertyVideo

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Number of extra forms to display for adding images

class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1  # Number of extra forms to display for adding videos

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'property_type', 'price', 'size', 'bedrooms', 'bathrooms', 'created_at')
    list_filter = ('location', 'property_type', 'bedrooms', 'bathrooms', 'created_at')
    search_fields = ('name', 'description', 'location', 'property_type')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'features', 'location', 'property_type', 'price', 'size')
        }),
        ('Media', {
            'fields': ('main_image', 'main_video')
        }),
        ('Details', {
            'fields': ('bedrooms', 'bathrooms')
        }),
    )
    inlines = [PropertyImageInline, PropertyVideoInline]  # Add this line to include inlines

    # Overriding the save method (if needed, otherwise, you can remove this)
    def save_model(self, request, obj, form, change):
        obj.save()

# Register the model with the customized admin
admin.site.register(Property, PropertyAdmin)
