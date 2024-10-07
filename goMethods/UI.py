"""
This module holds the UI.
"""
from datetime import datetime
from goMethods.Status import *


def ui(hashTable):
    # Loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Get the Status for all Packages")
        print("2. Get the Status for Package \'x\' (ID) at \'x\' Time (ex. \"8:00\")")
        print("3. Get the status of all Packages at \'x\' Time (ex. \"8:00\")")
        print("4. Exit the Program")
        option = input("Choose an option (1, 2, 3, or 4): ")

        if option == "1":
            getAllPkgStatus(hashTable)

        elif option == "2":
            # ID
            try:
                pID = int(input("Enter the ID of the package you want to know the status of (ex. 17): "))
                if pID <= 0:
                    raise ValueError

            except ValueError:
                print(f"\nSorry, \"{pID}\" is not a valid ID.")
                continue

            # Time
            try:
                userTime = input(f"For the status of package {pID}, please enter the time that you want to know for the"
                                 f" package's status: (ex. \"14:00\"): ")
                pTime = datetime.strptime(userTime, "%H:%M")  # Exception is thrown here
                toTime = timedelta(hours=pTime.hour, minutes=pTime.minute)

            except ValueError:
                print(f"\nSorry, \"{userTime}\" is not in a valid format (ex. \"14:00\").")
                continue

            # Get result
            getSinglePkgAtTime(hashTable, pID, toTime)

        elif option == "3":
            try:
                userTime = input("Enter the time for when you want to know the package statuses: (ex. \"14:00\"): ")
                pTime = datetime.strptime(userTime, "%H:%M")  # Exception is thrown here
                toTime = timedelta(hours=pTime.hour, minutes=pTime.minute)

            except ValueError:
                print(f"\nSorry, \"{userTime}\" is not in a valid format (ex. \"14:00\").")
                continue

            getTimeStatusAllPkgs(hashTable, toTime)

        elif option == "4":
            isExit = False

        else:
            print(f"\nSorry, \"{option}\" is not a valid option.")
            continue
