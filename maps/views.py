from django.shortcuts import render
from . import maps
import folium

# Create your views here.
def home(request):
    return render(request, 'maps.html')