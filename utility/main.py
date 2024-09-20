# Shlomo Pear 001504646
'''
Uses a self-adjusting heuristic algorithm to find a solution that delivers
all packages using under 140 miles and according to the provided
requirements (e.g., delivery deadlines, addresses, number of trucks,
special notes, etc.).

@FIXME
The wrong delivery address for package #9, Third District Juvenile
Court, will be corrected at 10:20 a.m. The correct address is “410 S
State St., Salt Lake City, UT 84111”

● Packages #13, #14, #15. #16, #19, and #20 must go out for delivery
on the same truck.
● Packages #3, #18, #36, and #38 may only be delivered by truck 2.
● #6, #25, #28, #32 cannot leave the hub before 9:05 a.m.

Always print out ALL attributes of the package:  ID, full address, deadline, delivery time, truck #


For the user interface, three (3) interface options are required:

1)   List the status of all packages.  When printing package status, show all attributes of the package class and the
truck that the package was assigned to.

2)   Request a specific package id and a time to show the status of the package at that time

3)   List the status of all packages – at a specific time



Suggestion: Code must be written to handle the use case where the user inputs a time that is earlier than the original
delivery of the package.  If this occurs, the package delivery would not be known and should be blank.   Additionally,
any arrival/address changes times must also be respected.  If you are unsure how to proceed, schedule an appointment
with a C950 Instructor.

datetime class use timedelta google it

'''
import csv
from datetime import time, timedelta

from model.Package import loadPackageData
from utility.Status import *
from utility.DistanceMethods import *


# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250
if __name__ == '__main__':
    print("Welcome Message")  #todo

    hashtable = ChainingHashTable()
    loadPackageData("../resource/WGUPS Package File.csv", hashtable) #fixme
    # hashtable.getPackageData()
    # todo Delivery.py methods go here

    # Distance data
    distanceList = loadDistanceData("../resource/WGUPS Distance Table.csv")

    # Address data
    addressList = loadAddressData("../resource/WGUPS Address File.csv")

    # Loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Get the Status for all Packages")
        print("2. Get the Status for Package \'x\' (ID) at \'x\' Time (ex. format example)")  #todo format example
        print("3. Get the status of all Packages at \'x\' Time (ex. format example)") #todo format example
        print("4. Exit the Program")
        option = input("Choose an option(1, 2, 3, or 4): ")
        if option == "1":
            getAllPkgStatus()

        elif option == "2":
            pID = int(input("Enter the ID of the package you want to know the status of (ex. 17): "))
            pTime = timedelta(input(f"For the status of package {pID}, please enter the time that you want to know" +
                                   " it's status: (ex. ): ")) #todo format example
            getSinglePkgAtTime(pID, pTime)

        elif option == "3":
            pTime = time(input("Enter the time you want to know the status of for all packages: (ex. ): ")) #todo format example
            #getTimeStatusAllPkgs(pTime)

        elif option == "4":
            isExit = False

        else:
            print(f"Sorry, \"{option}\" is not a valid option. Please enter a valid option (1, 2, 3, or 4).")
