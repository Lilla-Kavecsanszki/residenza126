from django.urls import path
from .views import all_properties, property_detail

urlpatterns = [
    path('properties/', all_properties, name='all_properties'),
    path('properties/<int:property_id>/', property_detail, name='property_detail'),
]
