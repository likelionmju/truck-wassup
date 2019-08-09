from django.shortcuts import render
from .models import FoodTruck
from account.models import Profile

def home(request):
    return render(request, 'home.html')

def detail(request):
    foodtrucks = FoodTruck.objects
    profiles = Profile.objects
    return render(request, 'detail.html', {'foodtrucks': foodtrucks}, {'profiles': profiles})
