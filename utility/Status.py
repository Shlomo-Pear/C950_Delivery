"""
This module holds the various methods that displays the statuses of packages. They are called in the main module.
"""
'''
@inquiry
Do I make this a utility method or make this a method of Package.py?

Allows the ‘user’ to check the status (at the hub, en route, or delivery
time) of any package at any given time.

Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   DELIVERY STATUS (I.E., AT THE HUB, EN ROUTE, OR DELIVERED), INCLUDING THE DELIVERY TIME

For the user interface, three (3) interface options are required:

1)   List the status of all packages.  When printing package status, show all attributes of the package class and the
truck that the package was assigned to.

2)   Request a specific package id and a time to show the status of the package at that time

3)   List the status of all packages – at a specific time



Suggestion: Code must be written to handle the use case where the user inputs a time that is earlier than the original
delivery of the package. If this occurs, the package delivery would not be known and should be blank. Additionally,
any arrival/address changes times must also be respected. If you are unsure how to proceed, schedule an appointment
with a C950 Instructor.
'''
from datetime import time, timedelta
from algorithms.Dijkstra import *
from algorithms.Greedy import *
from model.ChainingHashTable import *

# List the status of all packages. When printing package status, show all attributes of the package class and the
# truck that the package was assigned to.
def getAllPkgStatus():
    #todo add status info

    '''
    # Print out all packages
    truckID = -1
    for package in hashTable:
        # Get ID for the truck the packages are in
        if package in truck1:
            truckID = truck.id
        elif package in truck2:
            truckID = truck.id
        elif package in truck3:
            truckID = truck.id

        print(package + ", Truck #" + truckID)
        '''

# Request a specific package id and a time to show the status of the package at that time
def getSinglePkgAtTime(pID, time):
    #todo
    '''
    pack = hashTable.search(pID)
    status = ""

    # Checks to see if queried time is before delivered time
    if time < pack.time:
        status = "has yet to be"
    else:
        status = "has been"

    print(f"At time {time}, package #{pID} {status} delivered.")
'''

# List the status of all packages – at a specific time
'''def getTimeStatusAllPkgs(time):
    #todo
    for package in hashTable:
        status = ""
        if'''