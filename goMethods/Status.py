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

from datetime import timedelta
from model.Package import Package

"""
List the status of all packages. When printing package status, show all attributes of the package class and the truck
that the package was assigned to.
"""
def getAllPkgStatus(hashTable):

    correctPackage9(hashTable, timedelta(hours=10, minutes=20))

    # Search hash table for each package and print.
    print()
    print("Package Details")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")
    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)
        print(f"Package: {package}")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
# List the status and details of all packages at 'x' time.
"""
def getTimeStatusAllPkgs(hashTable, inputTime):

    # Correct package 9's details
    correctPackage9(hashTable, inputTime)

    # list of IDs for late packages that arrive at the hub at 9:05
    lateList = [6, 25, 28, 32]

    # inputTime is before 8:00 for regular packages
    time8 = timedelta(hours=8)
    # inputTime is before 9:05 for late packages
    time9o5 = timedelta(hours=9, minutes=5)

    # ----------------------------------------------------------
    # Search hash table for each package and print the status

    print()  # Blank space
    print(f"Status for All Packages At \"{inputTime}\"")
    print("------------------------------------------------------------------------------------------------------"
          "--------------------------------------------")

    for i in range(1, hashTable.count + 1):
        package = hashTable.search(i)

        # inputTime is before 8:00
        if inputTime < time8:
            status = "UNKNOWN"

        # Package arrived at the hub late
        elif (package.ID in lateList) and (inputTime < time9o5):
            status = "EN ROUTE TO HUB"

        # inputTime is before package left the hub
        elif inputTime < package.departureTime:
            status = "AT HUB"

        # inputTime is before the time the package was delivered
        elif inputTime < package.deliveryTime:
            status = "EN ROUTE"

        # inputTime is after the time the package was delivered
        else:
            status = "DELIVERED"

        if package.ID == 9 and package.truckNum is None:
            status = setPackage9Status(inputTime)
        # ----------------------------------------------------------

        message = f"Package {package.ID}\'s status at \"{inputTime}\":"

        print(f"{message}      {status}")
        print(f"   #{package}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
# ------------------------------------------------------------------------------------------------------


"""
Prints out the status and package details for 'x' package at 'x' time
"""


def getSinglePkgAtTime(hashTable, pID, inputTime):
    # Correct package 9's details
    correctPackage9(hashTable, inputTime)

    try:
        # list of IDs for late packages that arrive at the hub at 9:05
        lateList = [6, 25, 28, 32]

        # inputTime is before 8:00 for regular packages
        time8 = timedelta(hours=8)
        # inputTime is before 9:05 for late packages
        time9o5 = timedelta(hours=9, minutes=5)

        # search hashtable for package
        package = hashTable.search(pID)
        # ----------------------------------------------------------
        # Set Status

        # inputTime is before 8:00
        if inputTime < time8:
            status = "UNKNOWN"

        # Package arrived at the hub late
        elif (package.ID in lateList) and (inputTime < time9o5):
            status = "EN ROUTE TO HUB"

        # inputTime is before the package left the hub
        elif inputTime < package.departureTime:
            status = "AT HUB"

        # inputTime is before the time the package was delivered
        elif inputTime < package.deliveryTime:
            status = "EN ROUTE"

        # inputTime is after the time the package was delivered
        else:
            status = "DELIVERED"

        if package.ID == 9 and package.truckNum is None:
            status = setPackage9Status(inputTime)
        # ----------------------------------------------------------

        # Print results
        print(f"\nPackage {package.ID}\'s Status At \"{inputTime}\": {status}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")
        print(f"#{package}")
        print("------------------------------------------------------------------------------------------------------"
              "--------------------------------------------")

    except IndexError as e:
        print(f"\n{e}")


# ------------------------------------------------------------------------------------------------------


"""
This method corrects package 9's data if the input time is after 10:20
"""
def correctPackage9(hashTable, inputTime):

    # Correct package 9's address     Feels kind of messy putting this method here
    package = hashTable.search(9)

    # Time is after 10:20
    if inputTime >= timedelta(hours=10, minutes=20):
        package9 = Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD",
                           2, "Wrong address listed; address corrected")
        hashTable.insert(package9.ID, package9)

        # Update package details
        package9 = hashTable.search(9)
        package9.truckNum = package.truckNum
        package9.departureTime = package.departureTime
        package9.deliveryTime = package.deliveryTime
        # print(hashTable.search(9))

    # ----------------------------------------------------------

        # Time is before 10:20
    else:
        # Update package details to NA
        package.truckNum = None
        package.departureTime = timedelta()
        package.deliveryTime = timedelta()
        # print(hashTable.search(9))

# ------------------------------------------------------------------------------------------------------


"""
Sets the status for package 9
"""
def setPackage9Status(inputTime):

    # Sets the status
    # inputTime is before 8:00
    if inputTime < timedelta(hours=8):
        status = "UNKNOWN"

    # inputTime is after 8:00
    else:
        status = "AT HUB"

    return status
