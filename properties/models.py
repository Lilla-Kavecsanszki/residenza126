from django.db import models
from django.conf import settings

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
    main_image = models.ImageField(upload_to='images/', blank=True, null=True)  # Main image for cards
    main_video = models.FileField(upload_to='videos/', blank=True, null=True)  # Main video for cards
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()

    location = models.CharField(max_length=100, choices=LOCATIONS, default='Oristano')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='House')

    # Adding a ManyToManyField to track which users have liked this property
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_properties', blank=True)

    def __str__(self):
        return self.name

    def number_of_likes(self):
        """Returns the number of users who liked this property."""
        return self.liked_by.count()

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-created_at']  # Default ordering: most recent first


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.name}"


class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='property_videos/')

    def __str__(self):
        return f"Video for {self.property.name}"
    
