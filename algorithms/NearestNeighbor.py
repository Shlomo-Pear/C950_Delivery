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
Finds the next closest package and returns it and the distance between the two.
"""
def getClosestPackage(distanceData, addressList, truckPackages, startingAddress):

    minDistance = float('inf')
    nextPackage = None

    for package in truckPackages:
        address2 = package.address
        distance = distanceBetween(distanceData, addressList, startingAddress, address2)

        if distance < minDistance:
            minDistance = distance
            nextPackage = package

    return nextPackage, minDistance


"""
Returns the distance between two locations.
"""
def distanceBetween(distanceData, addressList, address1, address2):
    distance = 0

    h = addressList.index(address1)
    j = addressList.index(address2)

    # Mirror the addresses if there is no distance data for the vertex
    if distanceData[h][j] == '':
        distance = distanceData[j][h]
    else:
        distance = distanceData[h][j]

    return float(distance)

