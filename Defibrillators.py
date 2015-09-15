import sys
import math

lon = math.radians(float(raw_input().replace(',','.')))
lat = math.radians(float(raw_input().replace(',','.')))
n = int(raw_input())

min_distance  = ''
nearest_city = ''

for i in xrange(n):
    defib = raw_input()
    defib_details = defib.split(';;')
    city_name = defib_details[0].split(';')[1]
    city_coord = defib_details[1].split(';')
    city_lon = math.radians(float(city_coord[0].replace(',','.')))
    city_lat = math.radians(float(city_coord[1].replace(',','.')))
   
    x = (lon - city_lon) * math.cos((lat + city_lat)/2)
    y = (lat - city_lat)
    d = math.sqrt(x * x + y * y) * 6371

    if ( min_distance == ''):
        min_distance = d
        nearest_city = city_name
    else:
        if min_distance > d:
            min_distance = d
            nearest_city = city_name

print nearest_city
    
