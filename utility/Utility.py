"""
This module holds various utility methods.
"""
from datetime import timedelta


"""
Iterates through an inputted list of indexes and returns a list of the corresponding objects found within a hash table.
"""
def getItemsFromHashTable(hashTable, intList):
    outList = []
    for i in intList:
        hashObject = hashTable.search(i)
        outList.append(hashObject)
    return outList
# ----------------------------------------------------------


"""
Returns the elapsed time for the distance driven.
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
Gets the milage for each truck and the total milage
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
