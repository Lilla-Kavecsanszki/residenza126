from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Property
from profiles.models import UserProfile

@login_required
def like_property(request, property_id):
    """Handle like/unlike of a property."""
    property = get_object_or_404(Property, id=property_id)
    user = request.user

    if request.method == 'POST':
        # Get or create the user's profile
        user_profile, created = UserProfile.objects.get_or_create(user=user)

        if user in property.liked_by.all():
            # Unlike the property
            property.liked_by.remove(user)
            user_profile.liked_properties.remove(property)
        else:
            # Like the property
            property.liked_by.add(user)
            user_profile.liked_properties.add(property)

        # Redirect back to the referring page or home if not available
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))  # Redirect to referring page or home if not available
    else:
        # If not POST, just redirect to home or handle error
        return redirect(reverse('home'))


class AllProperties(View):
    def get(self, request, *args, **kwargs):
        """A view to show all properties, including sorting and search queries"""
        properties = Property.objects.all()
        query = request.GET.get('q', '')
        locations = request.GET.getlist('location')
        property_types = request.GET.getlist('type')
        sort = request.GET.get('sort', 'created_at')  # Default sorting field
        direction = request.GET.get('direction', 'asc')  # Default sorting direction

        # Debug: Print the filtering parameters
        print(f"Query: {query}")
        print(f"Locations: {locations}")
        print(f"Property Types: {property_types}")

        # Handle sorting
        valid_sort_keys = ['name', 'location', 'property_type', 'size', 'price', 'created_at']
        if sort in valid_sort_keys:
            if sort == 'name':
                properties = properties.annotate(lower_name=Lower('name'))
                sortkey = 'lower_name'
            else:
                sortkey = sort

            if direction == 'desc':
                sortkey = f'-{sortkey}'

            properties = properties.order_by(sortkey)
        else:
            messages.error(request, "Invalid sort option selected.")

        # Handle filtering by location
        if locations:
            filtered_locations = [loc for loc in locations if loc]  # Remove empty values
            if filtered_locations:
                properties = properties.filter(location__in=filtered_locations)

        # Handle filtering by property type
        if property_types:
            filtered_property_types = [ptype for ptype in property_types if ptype]  # Remove empty values
            if filtered_property_types:
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


class PropertyDetail(View):
    def get(self, request, property_id, *args, **kwargs):
        """A view to show individual property details"""
        property = get_object_or_404(Property, pk=property_id)
        liked = request.user.is_authenticated and property.liked_by.filter(id=request.user.id).exists()

        context = {
            'property': property,
            'images': property.images.all(),  # Fetch related images
            'videos': property.videos.all(),  # Fetch related videos
            'liked': liked,
        }
        return render(request, 'properties/property_details.html', context)





