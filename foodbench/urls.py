"""
URL configuration for foodbench project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tesstapp import views
from django.urls import path,include
from tesstapp.views import RestaurantViewSet, FoodItemViewSet 
from tesstapp import views
from django.urls import path
from tesstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_menu, name='restaurant_menu'),
    path('cart/', views.cart_page, name='cart_page'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('search_food/', views.search_food, name='search_food'),
    path('search_location/', views.search_location, name='search_location'),
    path('search/', views.search, name='search'),
]

