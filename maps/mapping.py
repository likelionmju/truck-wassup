import folium

add_address = 

#학교좌표 설정
default = folium.Map(location = [37.580421, 126.923437], zoom_start = 10)

folium.Marker([37.5, 126.9], popup = '테스트지점').add_to(default)

for index, row in 조사지점30.iterrows():
    folium.Marker(row.위경도, popup = row.조사지점명, radius = 3).add_to(default)