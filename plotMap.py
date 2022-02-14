import requests
from bs4 import BeautifulSoup
import folium
import getcoord

lis = ['Mehrgarh', 'Balochi', 'Neolithic','Kacchi Plain', 'Bolan Pass', 'Indus River', 'Pakistani', 'Quetta', 'Kalat', 'Sibi', 'Indus Valley', 'Indus Valley Civilization', 'Near-East', 'Mesopotamia', 'Near East', 'Mehrgarh,[32', 'India', 'Deccan Plateau', 'Neolithic Mehrgarh', 'Chalcolithic Mehrgarh', 'Iran', 'Middle East', 'Europe', 
'Persian Gulf', 'Asia', 'Indus River Valley', 'South Asia', 'Kili Gul Muhammad', 'Pakistan', 'Badakshan', 'Jalilpur', 'Togau', 'Nausharo', 
'Shahr', 'Sibri cemetery']
# print(len(lis))
j = 0
my_map3 = folium.Map(location = [20.5937, 78.9629],zoom_start = 3) 
folium.Marker([20.5937, 78.9629],popup = 'India').add_to(my_map3)
for i in lis:
    string = getcoord.find_links(i)
    coordinates = []
    try:
        lis2 = string.split('Coordinates')[1].split(' ')[:4]        
        if lis2[1][0]=='S':
            coordinates.append(float(lis2[0][:len(lis2[0])-1])*(-1))
        else:
            coordinates.append(float(lis2[0][:len(lis2[0])-1]))

        if lis2[3][0]=='W':
            coordinates.append(float(lis2[2][:len(lis2[2])-1])*(-1))
        else:
            coordinates.append(float(lis2[2][:len(lis2[2])-1]))
        j = j+1
        # print(coordinates, i)
        folium.Map(location = coordinates,zoom_start = 3).add_to(my_map3)
        folium.Marker(coordinates,popup = i).add_to(my_map3)
        continue
    except Exception as e:
        pass
    try:
        lis2 = getcoord.find_links(i).split(': ')[1].split(' ')[:3]
        coordinates.append(float(lis2[0][:6]))
        coordinates.append(float(lis2[1][:6]))
        j = j+1
        # print(coordinates, i)
        folium.Map(location = coordinates,zoom_start = 3).add_to(my_map3)
        folium.Marker(coordinates,popup = i).add_to(my_map3)
    except Exception as e:
        pass

# print(j)   No. of places marked

my_map3.save("index3.html ")   