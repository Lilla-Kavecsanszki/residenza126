from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Property
from django.shortcuts import render, get_object_or_404


def all_properties(request):
    """ A view to show all properties, including sorting and search queries """

    properties = Property.objects.all()
    query = request.GET.get('q', '')
    locations = request.GET.getlist('location')
    property_types = request.GET.getlist('type')
    sort = 'created_at'  # Default sorting field
    direction = 'asc'     # Default sorting direction

    # Debug: Print the filtering parameters
    print(f"Query: {query}")
    print(f"Locations: {locations}")
    print(f"Property Types: {property_types}")

    # Handle sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        valid_sort_keys = ['name', 'location', 'property_type', 'size', 'price', 'created_at']
        
        if sortkey in valid_sort_keys:
            if sortkey == 'name':
                properties = properties.annotate(lower_name=Lower('name'))
                sortkey = 'lower_name'
            elif sortkey in ['location', 'property_type', 'size', 'price', 'created_at']:
                sortkey = sortkey
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            properties = properties.order_by(sortkey)
        else:
            messages.error(request, "Invalid sort option selected.")

    # Handle filtering by location
    if locations:
        filtered_locations = [loc for loc in locations if loc]  # Remove empty values
        if filtered_locations:
            print(f"Filtering by locations: {filtered_locations}")
            properties = properties.filter(location__in=filtered_locations)

    # Handle filtering by property type
    if property_types:
        filtered_property_types = [ptype for ptype in property_types if ptype]  # Remove empty values
        if filtered_property_types:
            print(f"Filtering by property types: {filtered_property_types}")
            properties = properties.filter(property_type__in=filtered_property_types)

    # Handle search query
    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        properties = properties.filter(queries)

    # Get distinct choices for filters
    location_choices = Property.LOCATIONS
    property_types_choices = Property.PROPERTY_TYPES

    # Prepare current sorting key
    current_sorting = f'{sort}_{direction}'

    context = {
        'properties': properties,
        'search_query': query,
        'current_locations': locations,
        'current_property_types': property_types,
        'current_sorting': current_sorting,
        'location_choices': location_choices,
        'property_types_choices': property_types_choices,
    }

    return render(request, 'properties/properties.html', context)


def property_detail(request, property_id):
    """ A view to show individual property details """
    property = get_object_or_404(Property, pk=property_id)
    context = {
        'property': property,
    }
    return render(request, 'properties/property_details.html', context)

