from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Villa', 'Villa'),
        # Add other types as needed
    ]

    LOCATIONS = [
        ('Oristano', 'Oristano'),
        ('Torregrande', 'Torregrande'),
        ('Nolosodove', 'Nolosodove'),
        # Add other locations as needed
    ]
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    features = models.TextField(default='')
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Updated field
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()

    location = models.CharField(max_length=100, choices=LOCATIONS, default='Oristano')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='House')   

    def __str__(self):
        return self.name
