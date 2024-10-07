"""
The DistanceFile file holds methods that handles distance data.
"""
import csv
from model.Package import Package

"""
Loads package data from a .csv file into a hash table
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
    # Loads the package data from a file into a hash table
def loadPackageData(fileName, hashTable):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        next(packageData) # skips header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZCode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pNotes = package[7]

            # Package object
            package = Package(pID, pAddress, pCity, pState, pZCode, pDeadline, pWeight, pNotes)
            # print(package)

            # insert it into the hash table
            hashTable.insert(pID, package)


"""
Loads distance data from a .csv file into a list object
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
# Loads the distance data from a file into 2D list
def loadDistanceData(fileName):
    distanceArray = []
    count = 0
    with open(fileName) as distanceFile:
        distanceData = csv.reader(distanceFile, delimiter=',')
        # next(distanceData) # skips header

        # Add distanceData to distanceArray
        for i in distanceData:
            distanceArray.append(i)
            count += 1
            # print(i)
    # print(f"Total count of locations in distance file is: {count}")
    # print(distanceArray)
    return distanceArray


"""
Loads address data from a .csv file into a list object
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
# Loads the address data from a file into list
def loadAddressData(fileName):
    addressArray = []
    count = 0
    with open(fileName) as addressFile:
        addressData = csv.reader(addressFile, delimiter=',')
        next(addressData)  # skips header

        # Add distanceData to distanceArray
        for i in addressData:
            addressArray.append(i)
            count += 1
            # print(i)
    # print(f"Total count of locations in address file is: {count}")
    # print(addressArray)
    return addressArray
