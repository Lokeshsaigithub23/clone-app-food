<<<<<<< HEAD
from rest_framework import serializers
from .models import Restaurant, FoodItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'
=======
from rest_framework import serializers
from .models import Restaurant, FoodItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'
>>>>>>> 89753d7a3ee7e84d925c5a0aad0c3b4ce46fad57
