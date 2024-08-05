from django.db import models

class Property(models.Model):
    # Primary key is automatically created by Django, so no need to explicitly define Id
    
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    property_type = models.CharField(max_length=100, default='')
    features = models.TextField(default='')
    video_url = models.URLField(max_length=200, default='')
    image_url = models.URLField(max_length=200, default='')
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()  # Assuming size in square feet/meters

    def __str__(self):
        return self.name

