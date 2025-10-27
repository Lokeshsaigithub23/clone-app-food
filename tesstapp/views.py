from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializers import RestaurantSerializer, FoodItemSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Restaurant, FoodItem 
from django.db.models import Q

# Home Page
def home_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'tesstapp/home.html', {'restaurants': restaurants})

# Restaurant Detail Page

def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    food_items = FoodItem.objects.filter(restaurant=restaurant)
    context = {
        'restaurant': restaurant,
        'food_items': food_items,
    }
    return render(request, 'tesstapp/restaurant_menu.html', context)
# Cart Page
def cart_page(request):
    return render(request, 'tesstapp/cart.html')

# Login Page
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'tesstapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'tesstapp/login.html')

# Signup Page
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'tesstapp/signup.html', {'error': 'Username already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'tesstapp/signup.html')

# Django REST Framework ViewSets
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer 

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

#order tracking or food tracking

def order_page(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    food_items = FoodItem.objects.filter(restaurant=restaurant)
    total = sum(item.price for item in food_items)
    if not food_items.exists():
        message = "No menu items available. Please add something to order!"
    else:
        message = ""
    return render(request, 'tesstapp/order.html', {
        'restaurant': restaurant,
        'food_items': food_items,
        'total': total,
        'message': message
    })


#bill printing

def bill_page(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    order_items = FoodItem.objects.filter(restaurant=restaurant)
    total = sum(item.price for item in order_items)
    if not order_items.exists():
        message = "No items in menu. You can order something!"
    else:
        message = ""
    return render(request, 'tesstapp/bill.html', {
        'restaurant': restaurant,
        'order_items': order_items,
        'total': total,
        'message': message
    })


#comibed search
from django.shortcuts import render
from .models import Restaurant, FoodItem

def search_both(request):
    food_query = request.GET.get('food', '').strip()
    location_query = request.GET.get('location', '').strip()

    restaurant_food_dict = {}
    restaurant_results = Restaurant.objects.none()  # default empty
    no_restaurants_message = ""  # message to show if needed

    # Case 1: Only food query
    if food_query and not location_query:
        food_results = FoodItem.objects.filter(name__icontains=food_query)
        restaurant_results = Restaurant.objects.filter(id__in=food_results.values_list('restaurant_id', flat=True))
        for restaurant in restaurant_results:
            restaurant_food_dict[restaurant] = food_results.filter(restaurant=restaurant)

    # Case 2: Only location query
    elif location_query and not food_query:
        restaurant_results = Restaurant.objects.filter(location__icontains=location_query)
        for restaurant in restaurant_results:
            restaurant_food_dict[restaurant] = FoodItem.objects.filter(restaurant=restaurant)

    # Case 3: Both food + location
    elif food_query and location_query:
        # Restaurants in that location
        restaurant_results = Restaurant.objects.filter(location__icontains=location_query)
        # Only keep restaurants that have matching food
        matching_restaurants = []
        for restaurant in restaurant_results:
            matching_food = FoodItem.objects.filter(
                restaurant=restaurant,
                name__icontains=food_query
            )
            if matching_food.exists():
                matching_restaurants.append(restaurant)
                restaurant_food_dict[restaurant] = matching_food

        restaurant_results = Restaurant.objects.filter(id__in=[r.id for r in matching_restaurants])

        # If no restaurant has the food, set the message
        if not restaurant_results.exists():
            no_restaurants_message = f'No restaurants found for "{food_query}" in "{location_query}"'

    # Case 4: No filters
    else:
        restaurant_results = Restaurant.objects.all()
        for restaurant in restaurant_results:
            restaurant_food_dict[restaurant] = FoodItem.objects.filter(restaurant=restaurant)

    # Header text
    if food_query and location_query:
        header_text = f'Search Results for "{food_query}" in "{location_query}"'
    elif food_query:
        header_text = f'Search Results for "{food_query}"'
    elif location_query:
        header_text = f'Restaurants in "{location_query}"'
    else:
        header_text = "All Restaurants"

    return render(request, 'tesstapp/search_results.html', {
        'restaurant_results': restaurant_results,
        'restaurant_food_dict': restaurant_food_dict,
        'header_text': header_text,
        'food_query': food_query,
        'location': location_query,
        'no_restaurants_message': no_restaurants_message
    })
