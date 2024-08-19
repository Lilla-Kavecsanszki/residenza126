from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm  # Ensure the form name matches

@login_required
def user_profile(request):
    """A view to show the user's profile with login details."""
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # Create a profile if it does not exist
        profile = UserProfile.objects.create(user=user)

    form = UserProfileForm(instance=profile, user=user)  # Include the form in the context

    context = {
        'user': user,
        'profile': profile,
        'liked_properties': profile.liked_properties.all(),
        'form': form  # Pass the form to the template
    }

    return render(request, 'profiles/user_profile.html', context)

@login_required
def update_user_profile(request):
    """A view to update user profile information."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile')  # Ensure 'user_profile' is the correct URL name
    else:
        form = UserProfileForm(instance=request.user.userprofile, user=request.user)

    return render(request, 'profiles/user_profile.html', {'form': form})
