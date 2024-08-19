from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    default_phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your phone number'
        })
    )

    class Meta:
        model = UserProfile
        fields = ['default_phone_number']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        # Set initial values for first and last names if user is provided
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

        # Autofocus on the first field
        if self.fields:
            first_field = list(self.fields.keys())[0]
            self.fields[first_field].widget.attrs['autofocus'] = True
        
        # Add CSS class for each field
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean_default_phone_number(self):
        phone_number = self.cleaned_data.get('default_phone_number')
        if phone_number and not re.match(r'^\+?\d+$', phone_number):
            raise ValidationError("Phone number must contain only digits and optional leading '+'")
        return phone_number

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user = user_profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            user_profile.save()
        
        return user_profile
