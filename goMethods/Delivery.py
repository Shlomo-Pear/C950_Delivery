"""
This module holds the various methods used to make the project run. It uses a self-adjusting heuristic algorithm
(nearest neighbor) to find a solution that delivers all packages under 140 miles and according to the provided
requirements (e.g., delivery deadlines, addresses, number of trucks, special notes, etc.).
"""
from model.ChainingHashTable import ChainingHashTable
from model.Truck import Truck
from utility.LoadMethods import *
from utility.Utility import *
from algorithms.NearestNeighbor import *
from datetime import timedelta


"""
This method handles the setup and execution of the project.
It creates and fills a hash table with packages, fills trucks, and directs the truck departure order.
"""
def delivery():

    # Initialize hashtable, distance list, and address list
    hashTable = ChainingHashTable()
    loadPackageData("../resource/WGUPS Package File.csv", hashTable)
    # hashTable.getPackageData()

    # Distance data
    distanceList = loadDistanceData("../resource/WGUPS Distance Table.csv")

    # Address data
    addressList = loadAddressData("../resource/WGUPS Address File.csv")
    # print(addressList[0])

    # ----------------------------------------------------------
    # Initializes trucks and lists with package IDs and loads them onto the trucks

    # Test Check hashtable for all packages
    # hashTable.getPackageData()

    # Package IDs to load into trucks
    # Leaves at 8:00, Arrive by 10:30
    list1 = [1, 13, 14, 20, 29, 30, 31, 37, 40]

    # Leaves after 10:20, Correct address for package 9: “410 S State St., Salt Lake City, UT 84111”
    list2 = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 17, 18, 36, 38, 39]

    # Leaves after 9:05
    list3 = [21, 22, 23, 24, 26, 27, 28, 32, 33, 35]

    # Alternate more efficient truck lists (Unfinished)
    '''
    # list of IDs for packages with a deadline and that has to be grouped together
    deadlineList = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]

    # list of IDs for late packages that arrive at the hub at 9:05
    lateList = [6, 25, 28, 32]

    # list of IDs for packages that have to be on truck 2
    truck2List = [3, 18, 36, 38]
    truck2AddOns = [5, 9]

    # list of IDs for packages with end of day delivery
    eodDelivery = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 19, 21, 22, 23, 24, 26, 27, 29, 33, 35, 39]
    '''
    truck1 = Truck(ID=1)
    truck2 = Truck(ID=2)
    truck3 = Truck(ID=3)

    truck1.packages.extend([15, 16, 19, 34])  # Needs to be dropped off before 9:00
    truck2.packages.extend(list2)
    truck3.packages.extend([6, 25])  # Arrives late (9:05), 10:30 deadline
    # ----------------------------------------------------------
    # Trucks depart the HUB one at a time and drops off packages.

    # Truck 1 Leaves at 8:00
    truck1.timeLeftHub = timedelta(hours=8)
    truck1.timeAfterDelivery = truck1.timeLeftHub
    truckDeliverPackages(distanceList, addressList, truck1, hashTable)

    truck1TLH1 = truck1.timeLeftHub

    # Reload Truck
    truck1.packages.extend(list1)
    setDepartureTime(truck1, truck1)
    truckDeliverPackages(distanceList, addressList, truck1, hashTable)
    # ----------------------------------------------------------

    # Truck 3 before 2
    # Set departure time
    qTimeLeave = timedelta(hours=9, minutes=5)
    setDepartureTime(truck3, truck1, qTimeLeave)
    truckDeliverPackages(distanceList, addressList, truck3, hashTable)

    truck3TLH1 = truck3.timeLeftHub

    # Reload Truck
    truck3.packages.extend(list3)
    setDepartureTime(truck3, truck3)
    truckDeliverPackages(distanceList, addressList, truck3, hashTable)
    # ----------------------------------------------------------

    # Truck 2
    # Set departure time
    qTimeLeave = timedelta(hours=10, minutes=20)
    setDepartureTime(truck2, truck3, qTimeLeave)

    # Deliver the packages
    truckDeliverPackages(distanceList, addressList, truck2, hashTable)
    # ----------------------------------------------------------

    print(f"\nTruck operating times:")
    print(f"Truck 1: {truck1TLH1} - {truck1.timeAfterDelivery}")
    print(f"Truck 3: {truck3TLH1} - {truck3.timeAfterDelivery}")
    print(f"Truck 2: {truck2.timeLeftHub} - {truck2.timeAfterDelivery}")

    truckList = [truck1, truck2, truck3]
    return hashTable, truckList  # For UI


"""
determines the next package to deliver, tracks truck milage and time, drops off each package, and updates package details.
"""
def truckDeliverPackages(distanceList, addressList, truck, hashTable):

    # Starts off at HUB location
    nextAddress = addressList[0]

    # Drop off packages
    while len(truck.packages) > 0:

        # Gets the closest package
        nextPackageID, address, distanceToNext = getClosestPackage(
            hashTable, distanceList, addressList, truck.packages, nextAddress
        )

        nextAddress = address  # Updates the next address to the package delivery location
        truck.miles += distanceToNext  # Add distance traveled
        truck.location = nextAddress  # Set current truck location to the delivery address
        # ----------------------------------------------------------

        # Get time from truck and amount of time driven and update truck time
        truckTime = truck.timeAfterDelivery
        driveTime = getTravelTime(distanceToNext)
        deliveredAt = truckTime + driveTime
        truck.timeAfterDelivery = deliveredAt

        # Debug
        # print(f"Package ID: {nextPackageID}, Address: {address}, Distance: {distanceToNext}, "
        #      f"Delivered At: {deliveredAt}")

        # Get package
        # ----------------------------------------------------------

        # Add details to delivered package
        package = hashTable.search(nextPackageID)
        package.truckNum = truck.ID
        package.departureTime = truck.timeLeftHub
        package.deliveryTime = deliveredAt

        # Update hash table
        hashTable.insert(package.ID, package)

        truck.packages.remove(nextPackageID)
    # ----------------------------------------------------------
    # Return truck to hub
    truck.location = addressList[0]

