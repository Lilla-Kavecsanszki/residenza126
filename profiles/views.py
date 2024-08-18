from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import UserProfile

@login_required
def user_profile(request):
    """A view to show the user's profile with login details."""
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # Create a profile if it does not exist
        profile = UserProfile.objects.create(user=user)

    context = {
        'user': user,
        'profile': profile,
        'liked_properties': profile.liked_properties.all(),
    }

    return render(request, 'profiles/user_profile.html', context)
