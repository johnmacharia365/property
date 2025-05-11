from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, PropertyImage
from django.core.paginator import Paginator
from .forms import PropertyForm
# Create your views here.

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    images = PropertyImage.objects.filter(property=property)
    return render(request, 'listings/property_detail.html', {
        'property': property,
        'images': images
    })

def property_list(request):
    # Get all properties initially
    properties = Property.objects.all()

    # Apply filters if any are provided
    if 'q' in request.GET:
        properties = properties.filter(title__icontains=request.GET['q'])
    if 'location' in request.GET:
        properties = properties.filter(location__icontains=request.GET['location'])
    if 'min_price' in request.GET:
        properties = properties.filter(price__gte=request.GET['min_price'])
    if 'max_price' in request.GET:
        properties = properties.filter(price__lte=request.GET['max_price'])
    if 'property_type' in request.GET:
        properties = properties.filter(property_type=request.GET['property_type'])
    if 'availability' in request.GET:
        if request.GET['availability'] == 'available':
            properties = properties.filter(is_booked=False)
        elif request.GET['availability'] == 'booked':
            properties = properties.filter(is_booked=True)

    # Paginate the properties
    paginator = Paginator(properties, 9)  # Show 9 properties per page
    page_number = request.GET.get('page')
    properties = paginator.get_page(page_number)

    return render(request, 'listings/property_list.html', {'properties': properties})


def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        images = request.FILES.getlist('cover_image')
        if form.is_valid():
            property_instance = form.save()
            for image in images:
                PropertyImage.objects.create(property=property_instance, cover_image=image)
            return redirect('property_list')  # Redirect to the property list
    else:
        form = PropertyForm()

    return render(request, 'create_property.html', {'form': form})
