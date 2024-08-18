from django.db import models
from django.conf import settings
from properties.models import Property

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Add a ManyToManyField to track liked properties
    liked_properties = models.ManyToManyField(Property, related_name='liked_by_users', blank=True)

    def __str__(self):
        return self.user.username

    def number_of_liked_properties(self):
        """Returns the number of properties liked by the user."""
        return self.liked_properties.count()
