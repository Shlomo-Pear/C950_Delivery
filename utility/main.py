# Shlomo Pear 001504646
'''
Uses a self-adjusting heuristic algorithm to find a solution that delivers
all packages using under 140 miles and according to the provided
requirements (e.g., delivery deadlines, addresses, number of trucks,
special notes, etc.).


Always print out ALL attributes of the package:  ID, full address, deadline, delivery time, truck #


For the user interface, three (3) interface options are required:

1)   List the status of all packages.  When printing package status, show all attributes of the package class and the
truck that the package was assigned to.

2)   Request a specific package id and a time to show the status of the package at that time

3)   List the status of all packages – at a specific time

'''
from goMethods.Delivery import *
from goMethods.UI import *

# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250
if __name__ == '__main__':
    print("Welcome Message")  #todo

    hashTable = delivery()

    # Loop until user is satisfied
    ui(hashTable)
