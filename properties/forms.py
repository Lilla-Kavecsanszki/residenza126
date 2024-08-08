from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'location', 'property_type', 'features', 'video', 'image', 'bedrooms', 'bathrooms', 'price', 'size']
