#Compiled using python 2.7.10
#Creating one using geopy python library
import csv
import re
from geopy.geocoders import Nominatim

data_file = open('data_sci_snippet.csv')
csv_data_file = csv.reader(data_file)
list_price_str = []
list_price_num =[]
long_lat_coord = []

for row in csv_data_file:
    if row[8] != "GeoLat" and row[9] != "GeoLon":
        long_lat_coord.append(str(row[8])+", "+str(row[9]))

geolocator = Nominatim()
for i in long_lat_coord:
    try:
        location = geolocator.reverse(i)
        re.search(r"([^\s]+)?(\d{5})",str(location.address)).group(0)
        print (re.search(r"([^\s]+)?(\d{5})",str(location.address)).group(0))
    except Exception, e:
        print e

#Function to return median
def median(num_list):
    return num_list[len(num_list)/2] if len(num_list)%2 else (num_list[len(num_list)/2-1] + num_list[len(num_list)/2])/2

# #removing the header row
# for row in csv_data_file:
#     if row[7] != "LivingArea":
#         list_price_str.append(row[7])

# #Converting from string to int, removing white space errors
# for i in list_price_str:
#     try:
#         list_price_num.append(float(i))
#     except Exception, e:
#         pass

# #Report Results
# print "Median list price is $" + str(int(median(list_price_num)));









