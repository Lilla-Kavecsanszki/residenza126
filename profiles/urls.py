from django.urls import path
from .views import user_profile
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('update-profile/', views.update_user_profile, name='update_user_profile'),
]
