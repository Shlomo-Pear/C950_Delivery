"""
This class is the chaining hash table data structure that holds package data.


Dictionary ADTs prohibited

Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the
package ID as input and inserts each of the following data components into the hash table:
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time

"""


# Ref: zyBooks; Figure 7.8.2: Hash table using chaining. | WGU Webinar: Let's Go Hashing; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
# Modified for Key:Value
"""
HashTable class using chaining.
"""
class ChainingHashTable:

    """
    Constructor with optional initial capacity parameter.
    Assigns all buckets with an empty list.
    """
    def __init__(self, initial_capacity=10):
        # Initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

        self.count = 0

    # ----------------------------------------------------------

    """
    Inserts a new item into the hash table.
    """
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
        self.count += 1
        return True

    # ----------------------------------------------------------

    """
    Searches for an item with matching key in the hash table.
    Returns the item if found, or None if not found.
    """
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

        # If key is not in bucket
        raise IndexError(f'ID \'{key}\' not found in database')
        return None

    # ----------------------------------------------------------

    """
    Removes an item with matching key from the hash table.
    """
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # ----------------------------------------------------------

    """
    Method to fetch data from hash table by bucket
    """
    def getPackageData(self):
        for index, bucket in enumerate(self.table):
            for key, value in bucket:
                print(f"Key: {key} and Package: {value}")
