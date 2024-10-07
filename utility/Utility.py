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


"""
Returns the elapsed time for the distance driven.
"""
def getTravelTime(distance):
    speed = 18
    atTime = float(distance / speed)
    hours = int(atTime)
    minutes = int((atTime - hours) * 60)

    return timedelta(hours=hours, minutes=minutes)


"""
Sets the departure time for a given truck based on another truck's end delivery time.
"""
def setDepartureTime(potentialTime, currentTruck, previousTruck):
    # PreviousTruck's finishing time is before the potential departure time
    if previousTruck.timeAfterDelivery < potentialTime:
        currentTruck.timeLeftHub = potentialTime
    else:
        currentTruck.timeLeftHub = previousTruck.timeAfterDelivery

    currentTruck.timeAfterDelivery = currentTruck.timeLeftHub
