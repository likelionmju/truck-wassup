#!/usr/bin/env python
# coding: utf-8


import folium

def maps():
    map1 = folium.Map(location = [37.580421, 126.923437], zoom_start = 20)
    folium.Marker([37.580421, 126.923437], popup = 'Myongji University').add_to(map1)
    folium.Marker([37.581375, 126.924334], popup = '띵동와플').add_to(map1)
    map1.save('map.html')


