from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'location', 'price', 'property_type', 'is_booked', 'cover_image']
