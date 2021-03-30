#Ryan MacDonell CSE 42
#Project 3 - Ride Across the River
#83981682

from project3_mapquest_api import *
from project3_outputs import *

LOCATION_LIST = []
OUTPUT_LIST = []
x = '4533 Campus Dr, Irvine, CA'
y = '1111 Figueroa St, Los Angeles, CA'
z = '3799 S Las Vegas Blvd, Las Vegas, NV'

if __name__ == '__main__':
    input_locations = input()
    location_list = []
    for i in range(int(input_locations)):
        location_list.append(input())
    amount_of_outputs = input()
    output_list = []
    for i in range(int(amount_of_outputs)):
        output_list.append(input())
    locations = web_results(create_url(location_list))
    class_list = construct_class_list(output_list)
    if generate_output(locations, class_list) == 'MAPQUEST ERROR':
        print('MAPQUEST ERROR')
