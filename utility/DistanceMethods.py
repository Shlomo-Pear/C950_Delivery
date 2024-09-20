"""
The DistanceFile file holds methods that handle distance data
"""
import csv


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

# Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
    # Loads the address data from a file into list
def loadAddressData(fileName):
    addressArray = []
    count = 0
    with open(fileName) as addressFile:
        addressData = csv.reader(addressFile, delimiter=',')
        next(addressData) # skips header

        # Add distanceData to distanceArray
        for i in addressData:
            addressArray.append(i)
            count += 1
            # print(i)
    # print(f"Total count of locations in address file is: {count}")
    # print(addressArray)
    return addressArray