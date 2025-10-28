from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
  

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='restro-images/', null=True, blank=True)
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
    


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    food_items = models.ManyToManyField(FoodItem, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.user.username}'s Cart"

    def calculate_total(self):
        total = sum(item.price for item in self.food_items.all())
        self.total = total
        self.save()
        return total
    
    def update_total(self):
        total_price = sum(item.price for item in self.food_items.all())
        self.total = total_price
        self.save()



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Order Placed')  # e.g., Order Placed, Preparing, Delivered

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


