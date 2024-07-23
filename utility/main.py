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

datetime class use timedelta google it

'''
import csv
