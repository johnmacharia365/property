from django.db import models

# Property Model
class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('office', 'Office'),
        ('land', 'Land')
    ])
    is_booked = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='property_images/', default='property_images/list.jpeg')  # ✅ move this here

# PropertyImage Model
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to='property_images/',  # Folder where images will be saved
        null=True,  # Allow null for existing properties
        blank=True,  # Allow empty for the cover image in case it's not set
        default='property_images/list.jpeg'  # Default image if no cover image is provided
    )

    def __str__(self):
        return f"Image for {self.property.title}"
