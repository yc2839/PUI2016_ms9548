# Matt Sloane (ms9548)
# Homework 2 - Assignment 1: Tracking Each Vehicle for a Line

from __future__ import print_function

import pylab as pl
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
#%pylab inline


# Professor's script for number of arguments

###########################################

if not len(sys.argv) == 3:  # Assignment requires 2 arguments
    print("Invalid number of arguments. Run as: python  aSimplePythonScript.py YourNameHere")
    sys.exit()

###########################################

api_key = str(sys.argv[1])
bus_route = str(sys.argv[2])


#api_key_local = '68673bb3-d51c-4206-889a-8e8fa39ec14b'
#bus_route_local = 'B52'

mta_bus_api = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + api_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_route

response = urllib.urlopen(mta_bus_api)
data = response.read().decode("utf-8")
data = json.loads(data)

dict_nest = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
active_buses = len(dict_nest)

print ('Bus Line: ' + bus_route)
print ('Number of Active Buses: ' + str(active_buses))

for i in range(active_buses):
    j = str(dict_nest[i]['MonitoredVehicleJourney']['VehicleLocation'])
    print('Bus '+ str(i) + ' is at ' + j)
