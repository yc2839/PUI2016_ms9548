# Matt Sloane (ms9548)
# Homework 2 - Assignment 2: Next Stop Information

from __future__ import print_function

#import pylab as pl
#%pylab inline
import json
import sys
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


# Professor's script for number of arguments

###########################################

if not len(sys.argv) == 4:  # Assignment requires 3 arguments
    print("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHere")
    sys.exit()

###########################################

api_key = str(sys.argv[1])
bus_route = str(sys.argv[2])
csv_file = str(sys.argv[3])



#api_key_local = '68673bb3-d51c-4206-889a-8e8fa39ec14b'
#bus_route_local = 'B52'
mta_bus_api = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + api_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_route

response = urllib.urlopen(mta_bus_api)
data = response.read().decode("utf-8")
data = json.loads(data)

dict_nest_base = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
list_full = [['Latitude', 'Longitude', 'Stop_Name', 'Stop_Status']]

for i in dict_nest_base:
    
    list_temp = []
    
    lat = str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long = str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    
    try:
        stop = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
    
    except KeyError:
        stop = 'N/A'
        
    try:
        status = str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    
    except KeyError:
        status = 'N/A'
    
    list_temp = [lat, long, stop, status]
    list_full.append(list_temp)

list_full

busfile = open(csv_file, 'w')
writer = csv.writer(busfile)
writer.writerows(list_full)

#finally:
#    writer.close()
