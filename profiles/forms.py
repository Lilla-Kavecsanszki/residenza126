from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Autofocus on the first field
        if self.fields:
            first_field = list(self.fields.keys())[0]
            self.fields[first_field].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
                self.fields[field].widget.attrs['class'] = 'form-control'

        # Customizing the country field
        if 'default_country' in self.fields:
            self.fields['default_country'].widget.attrs['class'] = 'form-control'
