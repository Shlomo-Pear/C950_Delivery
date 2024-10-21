"""
This module holds methods that correct package 9's details.
Used in Status.py.
"""
from datetime import timedelta
from model.Package import Package


"""
This method corrects package 9's data if the input time is after 10:20
"""
def correctPackage9(hashTable, inputTime):
    # Correct package 9's address

    # Get package 9 non-parameter details
    deliveryDetails = hashTable.search(9)
    departureTime = deliveryDetails.departureTime
    deliveryTime = deliveryDetails.deliveryTime
    truckNum = deliveryDetails.truckNum

    # Time is after 10:20
    if inputTime >= timedelta(hours=10, minutes=20):
        package9 = Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD",
                           2, "Wrong address listed; address corrected")
        hashTable.insert(package9.ID, package9)

    # ----------------------------------------------------------

        # Time is before 10:20
    else:
        package9 = Package(9, "300 State St", "Salt Lake City", "UT", "84103", "EOD",
                           2, "Wrong address listed")
        hashTable.insert(package9.ID, package9)

# ------------------------------------------------------------------------------------------------------

    # Set non-parameter details
    package9.truckNum = truckNum
    package9.departureTime = departureTime
    package9.deliveryTime = deliveryTime


"""
Sets the status for package 9.
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

