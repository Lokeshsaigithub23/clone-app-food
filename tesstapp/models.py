<<<<<<< HEAD
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='restaurant_images/', null=True, blank=True)

    @property
    def image_url(self):
        """Safely return uploaded image URL or fallback"""
        if self.image:
            try:
                return self.image.url
            except ValueError:
                return '/static/default.jpg'
        return '/static/default.jpg'

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='food_items/', null=True, blank=True)

    @property
    def image_url(self):
        """Safely return uploaded image URL or fallback"""
        if self.image:
            try:
                return self.image.url
            except ValueError:
                return '/static/default_food.jpg'
        return '/static/default_food.jpg'

    def __str__(self):
        return self.name
=======
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    

class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu')
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
>>>>>>> 89753d7a3ee7e84d925c5a0aad0c3b4ce46fad57
