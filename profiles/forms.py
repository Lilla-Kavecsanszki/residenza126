from django import forms
from django.core.exceptions import ValidationError
import re
from .models import UserProfile

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['default_phone_number']
        widgets = {
            'default_phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
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
