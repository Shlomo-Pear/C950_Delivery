"""
This module holds the UI.


For the user interface, three (3) interface options are required:

1)   List the status of all packages.  When printing package status, show all attributes of the package class and the
truck that the package was assigned to.

2)   Request a specific package id and a time to show the status of the package at that time

3)   List the status of all packages – at a specific time

"""
from goMethods.Status import *
from datetime import datetime
from utility.Utility import getCountPackages


def ui(hashTable, truckList):

    # Loop until user is satisfied
    isExit = True
    while isExit:

        # Gets the number of packages in the hash table
        numPackages = getCountPackages(hashTable)
        # ----------------------------------------------------------
        print("***********************************************************************")
        print("\nOptions:")
        print("1. Get Truck Milage and the Details for All Packages")
        print("2. Get the Status of All Packages At \'X\' Time (ex. \"14:35\")")
        print("3. Get the Status for Package \'X\' (ID) at \'X\' Time (ex. \"14:35\")")
        print("4. Exit the Program")
        option = input("Choose an option (1, 2, 3, or 4): ")
        print("\n***********************************************************************")
        # ----------------------------------------------------------

        # Gets the details for all packages
        if option == "1":
            getAllPkgDetails(hashTable, truckList)
        # ----------------------------------------------------------

        # Gets the statuses and details for all packages at 'x' time
        elif option == "2":
            try:
                userTime = input("Enter the time for when you want to know each package status: (00:00 - 23:59) "
                                 "(ex. \"14:35\"): ")
                pTime = datetime.strptime(userTime, "%H:%M")  # Exception is thrown here
                toTime = timedelta(hours=pTime.hour, minutes=pTime.minute)

            except ValueError:
                print(f"\nSorry, \"{userTime}\" is not a valid time (00:00 - 23:59) (ex. \"14:35\")")
                continue

            getTimeStatusAllPkgs(hashTable, toTime)
        # ----------------------------------------------------------

        # Gets the status and details for 'x' package at 'x' time
        elif option == "3":
            # ID
            try:
                pID = input(f"Enter the ID of the package you want to know the status of (1 - {numPackages}) (ex. 17): ")
                pID = int(pID)
                if pID <= 0:
                    raise ValueError

            except ValueError:
                print(f"\nSorry, \"{pID}\" is not a valid ID (1 - {numPackages})")
                continue

            # Time
            try:
                userTime = input(f"Enter the time at which you want to check the status for package {pID} "
                                 f"(00:00 - 23:59) (e.g., \"14:35\"): ")
                pTime = datetime.strptime(userTime, "%H:%M")  # Exception is thrown here
                toTime = timedelta(hours=pTime.hour, minutes=pTime.minute)

            except ValueError:
                print(f"\nSorry, \"{userTime}\" is not a valid time (00:00 - 23:59) (ex. \"14:35\")")
                continue

            # Get result
            getSinglePkgAtTime(hashTable, pID, toTime)
        # ----------------------------------------------------------

        # Quit
        elif option == "4":
            print("\nGoodbye! (*^_^*)")
            isExit = False
        # ----------------------------------------------------------

        else:
            print(f"\nSorry, \"{option}\" is not a valid option.")
            continue
# ----------------------------------------------------------



