"""
This module holds methods that reads data from .csv files and loads it into tables and lists.

Todo add time complexity
"""

import csv
from model.Package import Package


"""
Loads package data from a .csv file into a hash table
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
def loadPackageData(fileName, hashTable):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        next(packageData)  # skips header
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
# ----------------------------------------------------------

"""
Loads distance data from a .csv file into a 2D list.
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
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
# ----------------------------------------------------------


"""
Loads address data from a .csv file into a list.
"""
# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
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
