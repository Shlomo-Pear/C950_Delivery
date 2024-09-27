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
from goMethods.Delivery import *
from goMethods.UI import *

# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250
if __name__ == '__main__':
    print("Welcome Message")  #todo

    delivery()

    # Loop until user is satisfied
    ui()
