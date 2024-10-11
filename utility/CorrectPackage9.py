"""
This module holds methods that correct package 9's details.
Used in Status.py.
"""
from datetime import timedelta
from model.Package import Package


"""
This method corrects package 9's data if the input time is after 10:20
"""
def correctPackage9(hashTable, originalPackage9, inputTime):

    # Correct package 9's address     Feels kind of messy putting this method here

    # Time is after 10:20
    if inputTime >= timedelta(hours=10, minutes=20):
        package9 = Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD",
                           2, "Wrong address listed; address corrected")
        hashTable.insert(originalPackage9.ID, package9)

        # Update package details
        package9 = hashTable.search(9)
        package9.truckNum = originalPackage9.truckNum
        package9.departureTime = originalPackage9.departureTime
        package9.deliveryTime = originalPackage9.deliveryTime
        # print(hashTable.search(9))

    # ----------------------------------------------------------

        # Time is before 10:20
    else:
        hashTable.insert(originalPackage9.ID, originalPackage9)

# ------------------------------------------------------------------------------------------------------


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

