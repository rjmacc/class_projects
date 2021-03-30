#Ryan MacDonell CSE 42
#Project 3 - Ride Across the River
#83981682

import project3_outputs
import urllib.request
import urllib.parse
import urllib.error
import json
import sys

API_KEY = 'eVp255FfJqKR0WgbybnXQciScnwBRcKP'
MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?'
ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def create_url(location_list):
    '''builds a url using the set API key from mapquest'''
    url_builder = [('key', API_KEY)]
    for i in range(len(location_list)):
        if i == 0:
            url_builder.append(('from', location_list[0]))
        else:
            url_builder.append(('to', location_list[i]))
    return MAPQUEST_URL + urllib.parse.urlencode(url_builder)

def create_elevation_url(coordinate_list):
    '''returns a list of urls containing for each locations elevation'''
    url_list = []
    for i in coordinate_list:
        url_builder = [('key', API_KEY),('latLngCollection', (i[0]+','+i[1]))]
        url_list.append(ELEVATION_URL + urllib.parse.urlencode(url_builder))
    return url_list

def web_results(url):
    ''' using the url, it will return a dictionary of strings'''
    web_location = None
    try:
        web_location = urllib.request.urlopen(url)
        web_data = web_location.read()
        #print(web_data)
        #print(type(web_data))
        data_str = web_data.decode(encoding= 'utf-8')
        if web_location != None:
            web_location.close()
        #print(type(data_str))
        #print(type(json.loads(data_str)))
        return json.loads(data_str)
    except:
        print('failure')
