from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import language_switch, handler404
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('properties/', include('properties.urls')),
    path('construction/', include('construction.urls')), 
    path('contact/', include('contact.urls')),
    path('language/<str:lang_code>/', language_switch, name='language_switch'),
    path('switch-language/<str:lang_code>/', views.language_switch, name='language_switch'),
]

# Adding i18n_patterns to handle language prefixes
urlpatterns += i18n_patterns(
    path('', include('residenza.urls')),  # Include your app's URLs with language prefixes
    prefix_default_language=False  # Optional: Set to True to remove default language prefix
)

# Serve static files (only in development, for production use a web server)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 error handler
handler404 = 'residenza126.views.handler404'
