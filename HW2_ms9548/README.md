Note - I attended the Wednesday evening office hours for part-time students with full-time jobs, which, per the professor's e-mail, permitted for later submission of the assignment.

#Homework 2

###Assignment 1
This code loops through the MTA SIRI API via the MTA Bus Time for Developers for lat / long data for active buses (my key: 68673bb3-d51c-4206-889a-8e8fa39ec14b).  The number of active buses was calculated by getting the length of the 'VehicleActivity' nested dictionary.  Kelsey Reid (kdr276) helped me located the nested dictionary level to use for the lat / long data (it was difficult to determine how exactly to dig down into the various nested dictionaries).  I also utilized the code the professor provided to accept arguments for Python Scripts.

###Assignment 2

This code loops through the MTA SIRI API to obtain lat, long, bus stop, and distance to next bus stop data - adding the individial unique bus data to a temporary list, then appending that to a global nested list, then ultimately writing that nested list to a .CSV file (Professor Bianco assisted me a CSV writing difficulty I was having).  I had initially developed the following loop code:

for i in range(active_buses):
    list_temp = []
    lat = str(dict_nest_base[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long = str(dict_nest_base[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    stop = str(dict_nest_base[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][i]['StopPointName'])
    status = str(dict_nest_base[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][i]['Extensions']['Distances']['PresentableDistance'])             
    list_temp = [lat, long, stop, status]
    list_full.append(list_temp)

It was only partially working.  William Xia helped me clarify the loop and I ultimately used something that parallels the code he used.

