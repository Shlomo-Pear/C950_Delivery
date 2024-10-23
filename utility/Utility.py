"""
This module holds various utility methods.
"""
from datetime import timedelta

from utility.CorrectPackage9 import setPackage9Status

"""
Iterates through an inputted list of indexes and returns a list of the corresponding objects found within a hash table.
*Not needed. Decided to go with just IDs in the truck package list instead and only getting one package's details at a time.

Complexity:
Space/Time: O(n)
"""
def getItemsFromHashTable(hashTable, intList):
    outList = []
    for i in intList:
        hashObject = hashTable.search(i)
        outList.append(hashObject)
    return outList
# ----------------------------------------------------------


"""
Returns the number of packages in the hash table.
Used in UI.py.
*Not needed

Complexity:
Time: O(n)
"""
def getCountPackages(hashTable):
    count = 0
    for i in range(1, hashTable.count + 1):
        count += 1

    return count
# ----------------------------------------------------------


"""
Returns the elapsed time for the distance driven.
Used in NearestNeighbor.py.

Complexity:
Time = O(1)
"""
def getTravelTime(distance):

    speed = 18
    atTime = float(distance / speed)

    hours = int(atTime)
    minutes = int((atTime - hours) * 60)

    return timedelta(hours=hours, minutes=minutes)
# ----------------------------------------------------------


"""
Sets the departure time for a given truck based on another truck's end delivery time.
Used in Delivery.py.

Complexity:
Time = O(1)
"""
def setDepartureTime(currentTruck, previousTruck, potentialTime=timedelta()):
    # If the current time (previousTruck's finishing time) is before the potential departure time, wait until then for
    # the currentTruck to leave the hub. Otherwise, the currentTruck's departure time is whenever the previousTruck
    # returned to hub.

    if previousTruck.timeAfterDelivery < potentialTime:
        currentTruck.timeLeftHub = potentialTime
    else:
        currentTruck.timeLeftHub = previousTruck.timeAfterDelivery

    # Set the current time to the departure time
    currentTruck.timeAfterDelivery = currentTruck.timeLeftHub


"""
Gets the milage for each truck and the total milage.
Used in Status.py.

Complexity:
Time: 0(n) 
"""
def getTruckMiles(truckList):

    totalMiles = 0.0

    print("\nTruck Miles:")
    for truck in truckList:  # Gets the milage for each truck
        totalMiles += truck.miles
        print(f"Truck {truck.ID} miles: {truck.miles:.2f}")

    # Gets the total miles
    print("-------------")
    print(f"Total miles:   {totalMiles:.2f}")
    print("----------------------")
    # ----------------------------------------------------------


"""
Gets the status for 'x' package at 'x' time, it's departure time, delivery time, and truck number it was on. 

Status may be UNKNOWN, EN ROUTE TO HUB, AT HUB, EN ROUTE, or DELIVERED.
Used in Status.py.

Complexity:
Space/Time: O(n)
"""
def getStatus(inputTime, package):

    # list of IDs for late packages that arrive at the hub at 9:05
    lateList = [6, 25, 28, 32]  # O(n)

    # inputTime is before 8:00 for regular packages
    time8 = timedelta(hours=8)
    # inputTime is before 9:05 for late packages
    time9o5 = timedelta(hours=9, minutes=5)

    departureTime = "NA"
    deliveryTime = "NA"
    truckNum = "NA"
    # ----------------------------------------------------------
    # Compares the input time to package time details and assigns status

    # inputTime is before 8:00
    if inputTime < time8:
        status = "UNKNOWN"

    # Package arrived at the hub late
    elif (package.ID in lateList) and (inputTime < time9o5):  # O(n)
        status = "EN ROUTE TO HUB"

    # inputTime is before package left the hub
    elif inputTime < package.departureTime:
        status = "AT HUB"

    # inputTime is before the time the package was delivered
    elif inputTime < package.deliveryTime:
        status = "EN ROUTE"
        departureTime = f"{package.departureTime}"
        truckNum = f"{package.truckNum}"

    # inputTime is after the time the package was delivered
    else:
        status = "DELIVERED"
        departureTime = f"{package.departureTime}"
        deliveryTime = f"{package.deliveryTime}"
        truckNum = f"{package.truckNum}"

    # Package 9 has the original address
    if package.ID == 9 and package.address == "300 State St":

        # inputTime is before 8:00
        if inputTime < time8:
            status = "UNKNOWN"
        # inputTime is after 8:00
        else:
            status = "AT HUB"

        # status = setPackage9Status(inputTime)  #O(1) Dropped. Opted to add this above ^.
        departureTime = "NA"
        deliveryTime = "NA"
        truckNum = "NA"
    # ----------------------------------------------------------

    return status, departureTime, deliveryTime, truckNum
