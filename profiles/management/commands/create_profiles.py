from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Command(BaseCommand):
    help = 'Create UserProfile for all existing users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profiles:
            UserProfile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created profile for user {user.username}'))
