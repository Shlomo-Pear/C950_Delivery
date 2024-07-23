"""
Dictionary ADTs prohibited

Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time

"""
import csv

from model.Package import Package


# Ref: zyBooks; Figure 7.8.2: Hash table using chaining. | WGU Webinar: Let's Go Hashing; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
# Modified for Key:Value

# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where the item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for key_value in bucket_list:
            # print(key_value)
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Ref: WGU Webinar: Getting Greedy, who moved my data?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256
    # Loads the package data from a file into a hash table
    def loadPackageData(self, fileName):
        with open(fileName) as packageFile:
            packageData = csv.reader(packageFile, delimeter=',')
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
                self.insert(pID, package)

'''
# Fetch data from hash table
for i in range(len(hashTable.table)+1):
    print(f"Key: {i+1} and Package: {hashTable.search(i+1)}")
'''