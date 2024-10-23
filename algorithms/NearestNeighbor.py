"""
This is the nearest neighbor algorithm that finds the next closest package.
"""
from utility.LoadMethods import loadDistanceData, loadAddressData

"""
Finds the next closest package and returns the ID, address, and the distance between it and the truck.

Space/Time Complexity = O(n^2)
"""
def getClosestPackage(hashTable, truckPackages, startingAddress):
    # Initialize
    count = 0  # For bug testing
    nextPackageID = -1
    minDistance = float('inf')

    # Search the hash table for the package's address and get the distance between truck and package
    # Complexity: Time: O(n)
    for i in truckPackages:
        count += 1
        package = hashTable.search(i)
        address2 = [package.address]

        # Print debug information
        # print(f"{count}\nStarting address: {startingAddress}, Address 2: {address2}")
        # ----------------------------------------------------------

        distance = distanceBetween(startingAddress, address2)  # Space/Time Complexity = O(n^2)
        # print(f"Testing distance: {distance}")

        # If the new distance is smaller, reassign variables
        if distance < minDistance:
            minDistance = distance
            nextPackageID = i
            nextPackageAddress = address2

    return nextPackageID, nextPackageAddress, minDistance

# -----------------------------------------------------------------------------------------------------


"""
Returns the distance between two locations.
Complexity:
Insertion: O(n^2)
Access:    O(1)
"""
def distanceBetween(address1, address2):

    # Distance data
    distanceData = loadDistanceData("../resources/WGUPS Distance Table.csv")

    # Address data
    addressList = loadAddressData("../resources/WGUPS Address File.csv")
    # print(addressList[0])
    # ----------------------------------------------------------

    # Assign h and j
    # Skip Header if index is 0 (0 = row/column header)
    h = addressList.index(address1)
    if h == 0:
        h += 1

    j = addressList.index(address2)
    if j == 0:
        j += 1

    # Debug
    # print(f"h index: {h}, j index: {j}")
    # print(f"Distance between {address1} and {address2}: {distanceData[h][j]}")

    # ----------------------------------------------------------
    # Finds the distance value

    # If addresses match or distance for vertex (un)mirrored is 0.0
    if address1 == address2:
        return 0.0
    if distanceData[j][h] == '0.0' and distanceData[h][j] == '0.0':
        return 0.0
    # --------------------------------

    # Mirror the addresses if there is no distance data for the vertex.
    if distanceData[h][j] == '':
        return float(distanceData[j][h])
    if distanceData[j][h] == '':
        return float(distanceData[h][j])
    # --------------------------------

    # Mirror the addresses if the distance is 0.0 and distance data exists for the mirror.
    if distanceData[h][j] == '0.0' and distanceData[j][h] != '':
        return float(distanceData[j][h])
    if distanceData[j][h] == '0.0' and distanceData[h][j] != '':
        return float(distanceData[h][j])
    else:
        return float(distanceData[h][j])
