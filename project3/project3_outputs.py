#Ryan MacDonell CSE 42
#Project 3 - Ride Across the River
#83981682

import project3_mapquest_api

def get_latlng(route):
    '''returns a list of tuples containing the lat and long of each location in the JSON response parameter'''
    coordinates = []
    for x in route['route']['locations']:
        coordinates.append(tuple((str((x['displayLatLng']['lat'])),(str(x['displayLatLng']['lng'])))))
    return coordinates

class steps:
    def output(self, location):
        '''prints the step by step directions'''
        print('DIRECTIONS')
        steps = location['route']['legs']
        for rifat in steps:
            for chowdhury in rifat['maneuvers']:
                print(chowdhury['narrative'])
        return ''
        
class total_distance:
    def output(self, location):
        '''prints the total distance traveled if completing the whole trip'''
        print('TOTAL DISTANCE: ' + str(int(location['route']['distance']+.5)) + ' miles')
        return ''
        
class total_time:
    def output(self, location):
        '''prints the total estimated time to complete the entire trip'''
        legs = location['route']['legs']
        time = 0
        for i in legs:
            time += get_time_in_mins(i['formattedTime'])
            
        print('TOTAL TIME: ' + str(time) + ' minutes')
        return ''

class lat_long:
    def output(self, location):
        '''prints the latitude and longitude of each of the locations'''
        print('LATLONGS')
        for i in location['route']['locations']:
            if float(i['displayLatLng']['lat']) > 0:
                latitude = 'N'
                lat_number = float(i['displayLatLng']['lat']) 
            elif float(i['displayLatLng']['lat']) < 0:
                latitude = 'S'
                lat_number = float(i['displayLatLng']['lat'] * -1) 
            else:
                latitude = '0'
                lat_number = 0
            if float(i['displayLatLng']['lng']) > 0:
                longitude = 'E'
                lng_number = float(i['displayLatLng']['lng'])
            elif float(i['displayLatLng']['lng']) < 0:
                longitude = 'W'
                lng_number = float(i['displayLatLng']['lng'] * -1)
            else:
                longitude = '0'
                lng_number = 0
            print('{:.2f}{} {:.2f}{}'.format(lat_number, latitude, lng_number, longitude))
            return ''
                      

class elevation:
    def output(self, location):
        '''prints the elevation(in ft.) of each of the specified locations'''
        print('ELEVATION')
        lat_long = get_latlng(location)
        for i in project3_mapquest_api.create_elevation_url(lat_long):
            for j in project3_mapquest_api.web_results(i)['elevationProfile']:
                print(str(int(j['height'] * 3.28+.5)))
        return ''
        
def get_time_in_mins(time:str):
    mins = 0
    time_list = time.split(':')
    mins += int(time_list[0]) * 60
    mins += int(time_list[1])
    mins += int((float(time_list[2]) / 60)+ .5)
    return mins

def construct_class_list(output_list):
    '''sets up classes based upon the output list that was inputted'''
    class_list = []
    for i in output_list:
        if i == 'STEPS':
            class_list.append(steps)
        elif i == 'TOTALDISTANCE':
            class_list.append(total_distance)
        elif i == 'TOTALTIME':
            class_list.append(total_time)
        elif i == 'LATLONG':
            class_list.append(lat_long)
        elif i == 'ELEVATION':
            class_list.append(elevation)

    return class_list

def generate_output(location, class_list):
    '''main function to print all the outputs'''
    try:
        for i in class_list:
            print(i.output(i, location))
    except:
        print('NO ROUTE FOUND')
    finally:
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreet Map Contributors')
