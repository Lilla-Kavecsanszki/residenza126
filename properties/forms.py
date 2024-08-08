from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name', 
            'description', 
            'features', 
            'video', 
            'image', 
            'bedrooms', 
            'bathrooms', 
            'price', 
            'size'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'features': forms.Textarea(attrs={'rows': 3}),
        }
