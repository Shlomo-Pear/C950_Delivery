"""
This module holds the various methods that displays the statuses of packages. They are called in the main module.

Allows the user to check:
    The details for all packages
    The status and details for all packages at 'x' time
    The status and details for package 'x' at 'x' time

Possible statuses:
    UNKNOWN
    AT HUB
    EN ROUTE
    DELIVERED

"""

from utility.Utility import getTruckMiles, getStatus
from utility.CorrectPackage9 import *

"""
List the status of all packages. When printing package status, show all attributes of the package class and the truck
that the package was assigned to.

Complexity:
Time: O(n)
"""
def getAllPkgDetails(hashTable, truckList):

    correctPackage9(hashTable, timedelta(hours=23, minutes=59))  # Time: O(1)

    # Get truck milage
    getTruckMiles(truckList)  # Time: O(n)

    print()
    print("Package Details")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")

    # Search hash table for each package and print. Time: O(n)
    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)

        departedAt = package.departureTime
        deliveredAt = package.deliveryTime
        truckNum = package.truckNum

        print(f"Package: {package}, Departed HUB At: {departedAt}, Delivered At: {deliveredAt} | Truck #{truckNum}")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
# List the status and details of all packages at 'x' time.

Complexity:
Space/Time: O(n)
"""
def getTimeStatusAllPkgs(hashTable, inputTime):

    # Correct package 9's details
    correctPackage9(hashTable, inputTime)  # O(1)

    # Search hash table for each package and print the status

    print()  # Blank space
    print(f"Status for All Packages At \"{inputTime}\"")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")

    # Get the status for each package    Time: O(n)
    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)
        status, departureTime, deliveryTime, truckNum = getStatus(inputTime, package)  # Space/Time: O(n)

        message = f"Package {package.ID}\'s status at \"{inputTime}\":"

        print(f"{message}      {status}")
        print(f"   #{package}, Departed HUB At: {departureTime}, Delivered At: {deliveryTime} | Truck #{truckNum}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
Prints out the status and package details for 'x' package at 'x' time

complexity:
# Space/Time: O(n)
"""
def getSinglePkgAtTime(hashTable, pID, inputTime):

    # Correct package 9's details
    correctPackage9(hashTable, inputTime)

    try:

        # search hashtable for package
        package = hashTable.search(pID)

        # Set Status
        status, departureTime, deliveryTime, truckNum = getStatus(inputTime, package)  # Space/Time: O(n)
        # ----------------------------------------------------------

        # Print results
        print(f"\nPackage {package.ID}\'s Status At \"{inputTime}\": {status}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
        print(f"#{package}, Departed HUB At: {departureTime}, Delivered At: {deliveryTime} | Truck #{truckNum}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")

    except IndexError as e:
        print(f"\n{e}")


# ------------------------------------------------------------------------------------------------------

