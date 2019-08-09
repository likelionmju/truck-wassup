from django.shortcuts import render, redirect
from .models import FoodTruck
from account.models import Profile

def home(request):
    return render(request, 'home.html')

def dev(request):
    return render(request, 'dev.html')

def detail(request):
    foodtrucks = FoodTruck.objects
    profiles = Profile.objects
    return render(request, 'detail.html', {'foodtrucks': foodtrucks}, {'profiles': profiles})

def register(request):
    if request.method == 'POST':
        foodTruck = FoodTruck()
        # company name
        foodTruck.name = request.POST['company']
        foodTruck.image = request.FILES['image']
        foodTruck.description = request.POST['description']
        foodTruck.save()
        return redirect('detail')
    return render(request, 'register.html')