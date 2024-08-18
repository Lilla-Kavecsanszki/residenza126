# properties/urls.py

from django.urls import path
from .views import AllProperties, PropertyDetail, like_property

urlpatterns = [
    path('properties/', AllProperties.as_view(), name='all_properties'),
    path('properties/<int:property_id>/', PropertyDetail.as_view(), name='property_detail'),
    path('like-property/<int:property_id>/', like_property, name='like_property'),
]
