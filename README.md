# C950_Delivery User Guide 

This project describes a traveling sailsman problem. It handles the delivery of packages from a hub location delivery
addresses by utilizing data structures and algorithms.
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

## Description of the Flow of the Code

\
In the main.py module, the program is split into two functions: one that handles the delivery, and the other that handles
the user interface (UI). I felt this would make the code easier to read than have either function completely written out
there.

The delivery function is the core of the project. It simulates the delivery of packages by truck over the course of the day
and tracks the time the packages left the hub, their time of delivery, and which truck they were driven on. The milage
of the trucks are also tracked.

The UI presents the data to the user as described in the above Directions.  

### Delivery

#### ______________ _Truck Management_ ______________

I start the function off by initializing a hash table and filling it with package data loaded in from a .csv file. I opted
to use a chaining hash table as it handles collisions really well and there is no need to constantly resize it if it gets
filled with lots of data, especially since it will only contain a very small amount of data (40 packages). That being said,
the table scales well when lots of data is added. There are two ways I would resize the table if this happens: manually
create another table with more buckets and fill it with the previous table's data and then empty the old one out, or create
a resizing function. The function would have a check to see if the table's data is a percentage over an arbitrary amount,
and if it is, it would create a new table within it with more buckets based off the square root of the total number of
packages, fill it, then replace the old table with the new one.

After this, I create lists of integers that correspond to the package IDs to fill three separate trucks that have a 
capacity for 16 packages at a time. Since the algorithm I'm using will determine which package to deliver one at a time,
it is simpler to search for a single one at a time there than to fill the lists with the package objects here. 

Truck 1 starts off at 8:00 AM. It makes two trips: one to deliver packages that if not delivered first, will not be
delivered on time/will prevent others from being delivered on time, and another to drop off the other packages with
deadlines.

Since truck 2 has to have certain packages on it that may be delivered by the end of the day (EOD), truck 3 goes next as
some packages will arrive at the hub late but (two of them) will still have a deadline. Like truck one, truck 3 will make
two trips to ensure the packages with deadlines are delivered on time. To ensure truck 2 does not exceed its carrying
capacity, truck 3 delivers some packages with an EOD deadline.

Truck 2 now delivers the remaining packages. Another reason why truck 2 goes last is because package 9's deadline is at
EOD, but the wrong address is listed for it and the correct address won't arrive until 10:20 AM. 

The directions allow for two trucks to run in parallel, but it was much easier to implement the trucks delivering the
packages in sequence. 

Finally, I print out the truck operating times. Although I'm not required to do so, I left it in since I found it helpful
for determining if packages with deadlines made it on time and I felt that the user will also find it helpful.

#### ________________ _Tracking Time_ ________________

The trucks have two attributes for tracking time: `timeLeftHub`, and `timeAfterDelivery`. The former is a timestamp which is
copied to a package's `timeLeftHub` attribute (which tracks its location) and is also used to determine the trucks'
operating times, while the latter determines the time the trucks leave the hub and at what time each package was delivered.

To ensure truck 3 doesn't leave before its packages arrive and truck 2 doesn't go before package 9's updated address comes,
I wrote a function that sets the departure time by comparing the time the last truck got back (the current time) to the
time the packages/details arrive at the hub (i.e. 9:05 or 10:20). if the current time is after they arrive, then the next
truck is fine to leave. Otherwise, it should wait to depart until then.

#### _______________ _Package Delivery_ _______________

There is a three part process to deliver the packages. The first part determines the next package the truck will deliver (1),
the second one tracks the time and the truck's milage (2), and the third part updates the package's details and removes the
package from the truck (3).

**1)** 
To determine this, I'm applying the nearest-neighbor algorithm. A for-loop iterates through the truck's list of package
IDs. Within each loop, the corresponding package is retrieved from the hashtable and the distance between the package's
destination and the hub/the previously delivered package's destination (the truck's current location) is retrieved from
a distance table This is then compared against a previously recorded distance (infinity to start with). If this one's
smaller, overwrite the package ID, the address, and the distance. Once all the IDs in the list are iterated through,
return the ID, address, and distance of the next closest address.

To get the correct distance, the index for the current location and the potential destination is first
      retrieved from a separate address table and is crossed-referenced in the distance table. If the index is '0' (the first
      index), the index will correspond to an address, not the distance between the two addresses, so in such a case '1' will
      need to be added to it so an error is not thrown. I can't just add '1' in all cases, since another error for going over
      the height/width will be thrown. (I bet there's a smarter/right way to go about this, but I can't think of it ¯\\\_(ツ)\_/¯.)
      Additionally, there are three kinds of checks to find the distance that pretty much boil down to if the distance is '0',
      if there is no distance data, or if there _is_ data. If it's the middle, then search from the opposite address
      (`distanceData[h][j]` → `distanceData[j][h]`). 

**2)** 
To determine the time the truck drove for, we use the function `time = distance / speed`. The distance was just determined,
and we also have the speed - 18 (See Assumptions above). We add this time to the truck's `timeAfterDelivery` attribute, which
starts off at the time the truck left the hub. We also add the distance to the truck's miles attribute.

**3)**
There are three package attributes that are updated: `truckNum`, `departureTime`, and `deliveryTime`. I think they are
pretty self-explanatory. Finally, the package is removed from the truck's package list. 

The process continues until there are no more packages remaining in the list.

### UI




_________
