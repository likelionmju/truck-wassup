#!/usr/bin/env python
# coding: utf-8


import folium

def maps():
    map1 = folium.Map(location = [37.580421, 126.923437], zoom_start = 20)
    folium.Marker([37.580421, 126.923437], popup = 'Myongji University').add_to(map1)
    folium.Marker([37.581515, 126.925015], popup = '띵동와플').add_to(map1)
    folium.Marker([37.580057, 126.924613], popup = '핫도그팩토리').add_to(map1)
    folium.Marker([37.579985, 126.925115], popup = '붕어빵').add_to(map1)
    folium.Marker([37.573945, 126.923334], popup = '타코야키').add_to(map1)
    folium.Marker([37.581752, 126.924334], popup = '청년반점').add_to(map1)
    folium.Marker([37.581375, 126.925334], popup = '키다리푸드트럭').add_to(map1)
    folium.Marker([37.581215, 126.921334], popup = '기도리').add_to(map1)
    folium.Marker([37.581175, 126.923434], popup = '청년창업').add_to(map1)
    folium.Marker([37.581475, 126.926234], popup = '꼬닐스').add_to(map1)
    map1.save('maps/templates/map.html')
    return map1
    
    




