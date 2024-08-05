from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
import logging

# Set up logging
logger = logging.getLogger(__name__)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact_submission.save()

            try:
                send_mail(
                    form.cleaned_data['subject'],  # Subject
                    f"Message from {form.cleaned_data['name']} "
                    f"<{form.cleaned_data['email']}>\n\n"
                    f"{form.cleaned_data['message']}",  # Message
                    None,  # From email (use default from email in settings.py)
                    ['earthalchemynaturals@example.com'],  # Recipient email
                )
                messages.success(
                    request,
                    'Thank you for your message! We will get back to you soon.'
                )
                return redirect('contact_us')
            except BadHeaderError:
                messages.error(
                    request,
                    'Invalid header found. Please try again.'
                )
                logger.error('Failed to send email due to invalid header.')
            except Exception as e:
                messages.error(
                    request,
                    'There was an error sending your message. Please try again later.'
                )
                logger.error(f'Failed to send email: {e}')
        else:
            messages.error(
                request,
                'Please correct the errors below.'
            )

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
