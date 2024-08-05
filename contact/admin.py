from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('subject',)
    ordering = ('-name',)  # Optionally order by name in descending order

    # Optional: Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'subject', 'message')
        }),
    )
    # Optional: Add custom form widgets or filters if needed
