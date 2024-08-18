from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile
from properties.models import Property

# Define an inline admin descriptor for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'
    fields = ('default_phone_number', 'liked_properties')
    readonly_fields = ('liked_properties',)  # You might not want to allow editing of liked properties here

# Define a custom admin class for the User model
class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

# Register the customized UserAdmin
admin.site.unregister(User)  # Unregister the original User admin
admin.site.register(User, UserAdmin)

# Register the UserProfile model separately (if needed)
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'number_of_liked_properties')
    search_fields = ('user__username', 'default_phone_number')
    readonly_fields = ('number_of_liked_properties',)
