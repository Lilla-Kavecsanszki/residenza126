from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Property

def all_properties(request):
    """ A view to show all properties, including sorting and search queries """

    properties = Property.objects.all()
    query = None
    locations = None
    property_types = None
    sort = None
    direction = None

    # Handle sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            properties = properties.annotate(lower_name=Lower('name'))
        elif sortkey == 'location':
            sortkey = 'location'
        elif sortkey == 'property_type':
            sortkey = 'property_type'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        properties = properties.order_by(sortkey)

    # Handle filtering by location
    if 'location' in request.GET:
        locations = request.GET['location'].split(',')
        properties = properties.filter(location__in=locations)

    # Handle filtering by property type
    if 'type' in request.GET:
        property_types = request.GET['type'].split(',')
        properties = properties.filter(property_type__in=property_types)

    # Handle search query
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search criteria!")
            return redirect(reverse('property_list'))

        queries = Q(name__icontains=query) | Q(
            description__icontains=query)
        properties = properties.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'properties': properties,
        'search_query': query,
        'current_locations': locations,
        'current_property_types': property_types,
        'current_sorting': current_sorting,
    }

    return render(request, 'properties/properties.html', context)

def property_detail(request, property_id):
    """ A view to show individual property details """

    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property,
    }

    return render(request, 'properties/property_detail.html', context)
