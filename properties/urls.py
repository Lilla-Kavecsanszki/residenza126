from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing all properties with sorting, filtering, and search
    path('', views.all_properties, name='all_properties'),  # Changed name to match view function

    # URL pattern for viewing details of a single property
    path('<int:property_id>/', views.property_detail, name='property_detail'),
]
