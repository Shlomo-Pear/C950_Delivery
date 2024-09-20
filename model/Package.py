import csv

class Package:
    def __init__(self, ID, address, city, state, zCode, deadline, weight, notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zCode = zCode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.deliverytime = None
        self.departureTime = None
        self.truckNum = None

    '''
    add 
    truck #
    delivery time
    left hub time
    '''
    def __str__(self): # Overwrites print(Package). Otherwise, it will print out the object reference.
        return f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zCode}, {self.deadline} deadline, {self.weight} kilos, Notes: {self.notes}"


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

