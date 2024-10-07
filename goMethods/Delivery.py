"""
This module holds the various methods used to make the project run. It loads up the hashtable, the trucks from the hash
table using a greedy algorithm, runs the trucks through the shortest-path-algorithm, and empties the trucks. The methods
are called in the main module.
"""
import datetime

from model.Truck import Truck
from goMethods.Status import *
from utility.LoadMethods import *
from utility.Utility import *
from algorithms.NearestNeighbor import *
from datetime import timedelta
"""
This method handles the setup and execution of the project.
It creates and fills a hash table with packages, fills trucks, and empties them at the destination. 
"""


def delivery():
    hashTable = ChainingHashTable()
    loadPackageData("../resource/WGUPS Package File.csv", hashTable)
    # hashTable.getPackageData()

    # Distance data
    distanceList = loadDistanceData("../resource/WGUPS Distance Table.csv")

    # Address data
    addressList = loadAddressData("../resource/WGUPS Address File.csv")
    # print(addressList[0])

    # Package IDs to load into trucks
    # Leaves at 8:00, Arrive by 10:30
    list1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
    # Leaves after 10:20, Correct address for package 9: “410 S State St., Salt Lake City, UT 84111”
    list2 = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 19, 36, 38, 39]
    # Leaves after 9:05
    list3 = [6, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35]

    truck1 = Truck(ID=1)
    truck2 = Truck(ID=2)
    truck3 = Truck(ID=3)

    truck1.packages.extend(list1)
    truck2.packages.extend(list2)
    truck3.packages.extend(list3)

    # Trucks depart the HUB one at a time.
    # Truck 1
    truck1.timeLeftHub = timedelta(hours=8)
    truck1.timeAfterDelivery = truck1.timeLeftHub
    truckDeliverPackages(distanceList, addressList, truck1, hashTable)

    # Truck 3 before 2
    # Set departure time
    qTimeLeave = timedelta(hours=9, minutes=6)
    setDepartureTime(qTimeLeave, truck3, truck1)

    # Deliver the packages
    truckDeliverPackages(distanceList, addressList, truck3, hashTable)

    # Truck 2
    # Set departure time
    qTimeLeave = timedelta(hours=10, minutes=21)
    setDepartureTime(qTimeLeave, truck2, truck3)

    # Correct package 9's address
    package9 = Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD",
                       2, "Wrong address listed; address corrected")
    hashTable.insert(package9.ID, package9)
    # print(hashTable.search(9))

    # Deliver the packages
    truckDeliverPackages(distanceList, addressList, truck2, hashTable)

    # Todo: Adjust package list so total miles are under 140
    # Test
    totalMiles = truck1.miles + truck2.miles + truck3.miles
    print(f"Truck 1 miles: {truck1.miles:.2f}")
    print(f"Truck 2 miles: {truck2.miles:.2f}")
    print(f"Truck 3 miles: {truck3.miles:.2f}")
    print(f"Total miles:   {totalMiles:.2f}")

    print(f"\nTruck operating times:")
    print(f"Truck 1: {truck1.timeLeftHub} - {truck1.timeAfterDelivery}")
    print(f"Truck 3: {truck3.timeLeftHub} - {truck3.timeAfterDelivery}")
    print(f"Truck 2: {truck2.timeLeftHub} - {truck2.timeAfterDelivery}")
    print(f"Package: {hashTable.search(6)}")

    return hashTable

"""
determines the next package to deliver, tracks truck milage and time, and drops off each package.
"""
def truckDeliverPackages(distanceList, addressList, truck, hashTable):

    # HUB location
    nextAddress = addressList[0]

    # Drop off packages
    while len(truck.packages) > 0:
        nextPackageID, address, distanceToNext = getClosestPackage(hashTable, distanceList, addressList, truck.packages,
                                                                   nextAddress)
        nextAddress = address
        truck.miles += distanceToNext
        truck.location = nextAddress

        # Get time from truck and amount of time driven
        truckTime = truck.timeAfterDelivery
        driveTime = getTravelTime(distanceToNext)
        deliveredAt = truckTime + driveTime

        # Update Truck's time
        truck.timeAfterDelivery = deliveredAt

        # Get package
        package = hashTable.search(nextPackageID)

        # Add details to delivered package
        package.truckNum = truck.ID
        package.departureTime = truck.timeLeftHub
        package.deliveryTime = deliveredAt

        # Update hash table
        hashTable.insert(package.ID, package)

        truck.packages.remove(nextPackageID)

    # Return truck to hub
    truck.location = addressList[0]
