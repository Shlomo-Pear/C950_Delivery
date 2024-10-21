# C950_Delivery
This project describes a traveling sailsman problem. It handles the delivery of packages from a hub location to other
locations by utilizing data structures and algorithms.
___

## Scenario

\
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution
for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised
deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day.
Each package has specific criteria and delivery requirements that are listed in the attached “WGUPS Package File.”

 

Your task is to determine an algorithm, write code, and present a solution where all 40 packages will be delivered on
time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for all
trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each
location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location
and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments
to make your code easy to follow and to justify the decisions you made while writing your scripts.

 

The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the
variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

___

## Assumptions

\
•  Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•  The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•  There are no collisions.

•  Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck
is in service.

•  Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.

•  The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to
a truck at the hub). This time is factored into the calculation of the average speed of the trucks.

•  There is up to one special note associated with a package.

•  The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS
is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address
(410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

•  The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.

•  The day ends when all 40 packages have been delivered.

___

## Directions

\
The output starts off with the operating times for the trucks. This isn't necessary, I just find it helpful. (It's stored
at the bottom of the delivery() function in Delivery.py)

Next, user input options (1 - 4) are displayed:
1) Get the total milage the trucks have driven and the final delivery information for all the packages.
2) Get the details for each package at a particular time.
3) get the details for a singular package at a particular time.
4) Exit the program.

Any other input will display an error message.

For options 1 - 3, the time the package left the hub, the time the package was delivered, and the truck number is included
in the information displayed.

For options 2 and 3, a status will be displayed to indicate where the package is located at the requested time. If after
the user enters one of these and then enters a non-integer for the package ID or a time format other than what's in the
example, an error message is displayed and input begins at the options menu again.

The time is in 24-hour format. The format only includes hours and minutes, not seconds (8:27:14 will display an error message).

Statuses can be UNKNOWN, EN ROUTE TO HUB, AT HUB, EN ROUTE, or DELIVERED.

If the user enters a time when the package is not DELIVERED, the extra data included with the package details will/may be
NA.

### Special Package Instructions __________________
##### Deadline ______
* Package 15 has a 09:00 deadline
* Packages 1, 6, 13, 14, 16, 20, 25, 29 - 31, 34, 37, and 40 have a 10:30 deadline
* All other packages can be delivered by the end of the day.

##### Groups _______
* Packages 6, 25, 28, and 32 won't arrive at the hub until 09:05.
* Package 9's address is incorrect and will not have the correct address data until 10:20.
* Packages 13 - 16, 19, and 20 have to be delivered on the same truck.
* Packages 3, 18, 36, and 38 must be delivered on truck 2.
___

## Justification of Flow

\

___
