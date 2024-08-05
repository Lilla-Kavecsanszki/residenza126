from django.shortcuts import render
from properties.models import Property  # Adjust the import path to reflect your project structure

def homepage(request):
    # Fetch properties or other data to pass to the template
    properties = Property.objects.all()  # Fetch all properties

    context = {
        'property_list': properties,  # Pass properties to the template under the key 'property_list'
    }

    return render(request, 'index.html', context)
