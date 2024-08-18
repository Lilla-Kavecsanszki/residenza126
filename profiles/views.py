from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import PhoneNumberForm


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
        'form': PhoneNumberForm(instance=profile)  # Include the form in the context
    }

    return render(request, 'profiles/user_profile.html', context)


@login_required
def update_phone_number(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Phone number updated successfully!')
            return redirect('user_profile')  # Ensure 'user_profile' is the correct URL name
    else:
        form = PhoneNumberForm(instance=request.user.userprofile)

    return render(request, 'profiles/user_profile.html', {'form': form})

