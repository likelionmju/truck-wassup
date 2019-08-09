from django.shortcuts import render
from . import maps
import folium
import os

# Create your views here.
def home(request):
    mark = maps.maps().get_root().render()
    #mark.split()
    #open("./templates/map.html", 'r')
    #open(os.path.join(STATIC_ROOT,'maps/templates/map.html'), 'r')
    return render(request, 'maps.html', {'mark':mark})