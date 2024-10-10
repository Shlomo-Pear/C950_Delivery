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
"""
def getAllPkgDetails(hashTable, truckList, originalPackage=None):

    correctPackage9(hashTable, originalPackage, timedelta(hours=17, minutes=30))

    # Get truck milage
    getTruckMiles(truckList)

    print()
    print("Package Details")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")

    # Search hash table for each package and print.
    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)
        print(f"Package: {package}, Departed HUB At: {package.departureTime}, Delivered At: {package.deliveryTime}, Truck #{package.truckNum}")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
# List the status and details of all packages at 'x' time.
"""
def getTimeStatusAllPkgs(hashTable, inputTime, originalPackage=None):

    # Correct package 9's details
    correctPackage9(hashTable, originalPackage, inputTime)

    # Search hash table for each package and print the status

    print()  # Blank space
    print(f"Status for All Packages At \"{inputTime}\"")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")

    # Get the status for each package
    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)
        status, departureTime, deliveryTime, truckNum = getStatus(inputTime, package)

        message = f"Package {package.ID}\'s status at \"{inputTime}\":"

        print(f"{message}      {status}")
        print(f"   #{package}, Departed HUB At: {departureTime}, Delivered At: {deliveryTime}, Truck #{truckNum}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
Prints out the status and package details for 'x' package at 'x' time
"""


def getSinglePkgAtTime(hashTable, pID, inputTime, originalPackage=None):

    # Correct package 9's details
    correctPackage9(hashTable, originalPackage, inputTime)

    try:

        # search hashtable for package
        package = hashTable.search(pID)

        # Set Status
        status, departureTime, deliveryTime, truckNum = getStatus(inputTime, package)
        # ----------------------------------------------------------

        # Print results
        print(f"\nPackage {package.ID}\'s Status At \"{inputTime}\": {status}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
        print(f"#{package}, Departed HUB At: {departureTime}, Delivered At: {deliveryTime}, Truck #{truckNum}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")

    except IndexError as e:
        print(f"\n{e}")


# ------------------------------------------------------------------------------------------------------

