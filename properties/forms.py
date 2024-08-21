from django import forms
from django.forms import inlineformset_factory
from .models import Property, PropertyImage, PropertyVideo

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'description',
            'features',
            'main_image',
            'main_video',
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
            'main_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'main_video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PropertyVideoForm(forms.ModelForm):
    class Meta:
        model = PropertyVideo
        fields = ['video']
        widgets = {
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# Formsets
PropertyImageFormSet = inlineformset_factory(
    Property,
    PropertyImage,
    form=PropertyImageForm,
    extra=5,  # Adjust the number of extra forms as needed
    can_delete=True,
    min_num=0,  # Enforce at least one image form
    validate_min=True
)

PropertyVideoFormSet = inlineformset_factory(
    Property,
    PropertyVideo,
    form=PropertyVideoForm,
    extra=5,  # Adjust the number of extra forms as needed
    can_delete=True,
    min_num=0,  # Enforce at least one video form
    validate_min=True
)
