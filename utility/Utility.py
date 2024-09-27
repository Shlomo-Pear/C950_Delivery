"""
This module holds various utility methods.
"""
"""
Iterates through an inputted list of indexes and returns a list of the corresponding objects found within a hash table.
"""
def getItemsFromHashTable(hashTable, intList):
    outList = []
    for i in intList:
        hashObject = hashTable.search(i)
        outList.append(hashObject)
    return outList
