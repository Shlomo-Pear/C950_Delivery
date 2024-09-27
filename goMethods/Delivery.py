"""
This module holds the various methods used to make the project run. It loads up the hashtable, the trucks from the hash
table using a greedy algorithm, runs the trucks through the shortest-path-algorithm, and empties the trucks. The methods
are called in the main module.
"""
"""
The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
"""

from model.Truck import Truck
from goMethods.Status import *
from utility.LoadMethods import *
from utility.Utility import *
from algorithms.NearestNeighbor import *

"""
This method handles the setup and execution of the project.
It creates and fills a hash table with packages, fills trucks, and empties them at the destination. 
"""


def delivery():
    preDelHashTable = ChainingHashTable()
    postDelHashTable = ChainingHashTable()
    loadPackageData("../resource/WGUPS Package File.csv", preDelHashTable)
    # preDelHashTable.getPackageData()

    # Distance data
    distanceList = loadDistanceData("../resource/WGUPS Distance Table.csv")

    # Address data
    addressList = loadAddressData("../resource/WGUPS Address File.csv")
    # print(addressList[0])

    # Correct package 9's address
    package9 = Package(9, "410 S State St", "Salt Lake City", "UT", "84111", "EOD",
                       2, "Wrong address listed; address corrected")
    preDelHashTable.insert(package9.ID, package9)
    # print(preDelHashTable.search(9))

    # Package indexes to load into trucks
    # Arrive by 10:30
    list1 = [1, 6, 13, 14, 15, 16, 19, 20, 25, 29, 30, 31, 34, 37, 40]
    # leave at 10:21, Correct address for package 9: “410 S State St., Salt Lake City, UT 84111”
    list2 = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 28, 32, 36, 38]
    list3 = [21, 22, 23, 24, 26, 27, 33, 35, 39]

    truck1 = Truck(ID=1, timeLeft="9:06")
    truck2 = Truck(ID=2, timeLeft="10:21")
    truck3 = Truck(ID=3)

    # Loops through truck package list and matches the IDs to the package in hash table and loads up the trucks
    truck1List = getItemsFromHashTable(preDelHashTable, list1)
    truck2List = getItemsFromHashTable(preDelHashTable, list2)
    truck3List = getItemsFromHashTable(preDelHashTable, list3)
    # print(truck1List[3])

    truck1.packages.extend(truck1List)
    truck2.packages.extend(truck2List)
    truck3.packages.extend(truck3List)

    # todo Nearest Neighbor Algorithm goes here. For every 18 miles (as determined by the package distance within the
    #  truck), one hour passes

    # Todo add the delivered package to postDelHashTable
'''
    truckDeliverPackages(distanceList, addressList, truck1, postDelHashTable)  # Truck1
    truckDeliverPackages(distanceList, addressList, truck2, postDelHashTable)  # Truck2
    truckDeliverPackages(distanceList, addressList, truck3, postDelHashTable)  # Truck3
'''

'''
D) Algorithm to Deliver Packages:

D.1) Function to deliver packages in a Truck:

15-Define truckDeliverPackages(truck)

16-Loop truck package addresses and call minDistanceFrom(fromAddress, truckPackages) for all the addresses not visited
yet

D.2) Keep track of miles and time delivered:

17-Update delivery status and time delivered in Hash Table for the package delivered and keep up with total mileage and
delivery times. 

    i.e. How to keep track of the time?:

    timeToDeliver(h) = distance(miles)/18(mph) where 18 mph average Truck speed. 

    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)). time_obj could be cumulated to keep
    track of time.
'''

"""
determines the next package to deliver, tracks truck milage, tracks time, and drops off each package.
"""
def truckDeliverPackages(distanceList, addressList, truck, hashTable):  # Todo
    nextAddress = addressList[0]  # HUB location

    # Tracks package status
    for package in truck.packages:
        package.status = "En Route"

    while len(truck.packages) > 0:
        nextPackage, distanceToNext = getClosestPackage(distanceList, addressList, truck.packages, nextAddress)
        nextAddress = nextPackage.address
        truck.miles += distanceToNext

        truck.packages.remove(nextPackage)

        # Add details to delivered package
        nextPackage.truckNum = truck.ID
        nextPackage.status = "Delivered"
        nextPackage.departureTime = truck.timeLeft
        nextPackage.deliveryTime = None  # Todo add time zachen

        hashTable.insert(nextPackage.ID, nextPackage)
