from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_properties, name='property_list'),  # Use 'all_properties' view here
    path('<int:property_id>/', views.property_detail, name='property_detail'),
]
