# forms.py
from django import forms
from .models import Property
from .widgets import CustomClearableFileInput

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'description',
            'features',
            'video',
            'image',
            'location',
            'property_type',
            'bedrooms',
            'bathrooms',
            'price',
            'size'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'features': forms.Textarea(attrs={'rows': 3}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'video': CustomClearableFileInput(attrs={'class': 'form-control'}),
            'image': CustomClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate location choices dynamically if needed
        self.fields['location'].choices = Property.LOCATIONS
        
        # Populate property_type choices dynamically if needed
        self.fields['property_type'].choices = Property.PROPERTY_TYPES

        # Apply CSS classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
