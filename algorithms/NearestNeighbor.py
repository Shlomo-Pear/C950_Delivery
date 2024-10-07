'''
Algorithm to Load Packages:

C.3) Function to load packages into Trucks:

12-Define truckLoadPackages()

13-Load Trucks based on assumptions provided (ex. Truck-2 must have some packages, some packages go together,
some packages are delayed, ...)

14-And closest addresses/packages until there is 16 packages in a Truck

  i.e. Load manually/heuristically or Loop package addresses and call minDistanceFrom(fromAddress, truckPackages) for
  all the addresses in the Truck not visited yet
'''


"""
Finds the next closest package and returns the ID, address, and the distance between it and the truck.
"""
def getClosestPackage(hashTable, distanceData, addressList, truckPackages, startingAddress):

    count = 0
    nextPackageID = -1
    minDistance = float('inf')

    # Search the hash table for the package's address and get the distance between truck and package
    for i in truckPackages:
        count += 1
        package = hashTable.search(i)
        address2 = [package.address]
        # print(f"{count})")
        # print(f"Starting address: {startingAddress}")
        # print(f"Address 2: {address2}")

        distance = distanceBetween(distanceData, addressList, startingAddress, address2)

        if distance < minDistance:
            minDistance = distance
            nextPackageID = i

    return nextPackageID, address2, minDistance


"""
Returns the distance between two locations.
"""
def distanceBetween(distanceData, addressList, address1, address2):

    h = addressList.index(address1) + 1
    j = addressList.index(address2)

    # Mirror the addresses if there is no distance data for the vertex
    if distanceData[h][j] == '':
        distance = distanceData[j][h]
    else:
        distance = distanceData[h][j]

    return float(distance)

