"""
This module holds the UI.
"""
from goMethods.Status import *


def ui():
    # Loop until user is satisfied
    isExit = True
    while isExit:
        print("\nOptions:")
        print("1. Get the Status for all Packages")
        print("2. Get the Status for Package \'x\' (ID) at \'x\' Time (ex. format example)")  # todo format example
        print("3. Get the status of all Packages at \'x\' Time (ex. format example)")  # todo format example
        print("4. Exit the Program")
        option = input("Choose an option(1, 2, 3, or 4): ")
        if option == "1":
            getAllPkgStatus()

        elif option == "2":
            pID = int(input("Enter the ID of the package you want to know the status of (ex. 17): "))
            pTime = timedelta(input(f"For the status of package {pID}, please enter the time that you want to know" +
                                    " it's status: (ex. ): "))  # todo format example
            getSinglePkgAtTime(pID, pTime)

        elif option == "3":
            pTime = time(input(
                "Enter the time you want to know the status of for all packages: (ex. ): "))  # todo format example
            # getTimeStatusAllPkgs(pTime)

        elif option == "4":
            isExit = False

        else:
            print(f"Sorry, \"{option}\" is not a valid option. Please enter a valid option (1, 2, 3, or 4).")