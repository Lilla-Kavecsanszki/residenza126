from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings

# Manually define LANGUAGE_SESSION_KEY if it's not available
LANGUAGE_SESSION_KEY = 'django_language'

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

def switch_language_view(request):
    user_language = request.GET.get('language', 'en')  # Default to English if no language is specified
    translation.activate(user_language)
    response = render(request, 'index.html')  # Replace 'your_template.html' with your actual template
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

import logging
logger = logging.getLogger(__name__)

def language_switch(request, lang_code):
    if lang_code in dict(settings.LANGUAGES):
        logger.debug(f"Switching language to: {lang_code}")
        request.session[LANGUAGE_SESSION_KEY] = lang_code
        translation.activate(lang_code)
    return redirect(request.META.get('HTTP_REFERER', '/'))