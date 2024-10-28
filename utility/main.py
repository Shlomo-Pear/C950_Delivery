# Shlomo Pear 001504646
"""
Mailing system program that loads up trucks with packages, determines the next location to drop off a package, tracks
the delivery statuses (UNKNOWN, AT HUB, EN ROUTE, DELIVERED) of the packages, and updates the package details with truck
number, departure time, and delivery time.
"""
# There are two parts to the project: The core module that handles the whole delivery aspect, and the UI. I decided to
# separate them into other modules than 'main' because I think it's easier to follow the flow of the code.

from goMethods.Delivery import *
from goMethods.UI import *


# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250
if __name__ == '__main__':
    print("WGU Mail Routing System")

    # Complexity:
    # Space: O(n^2)
    # Time: O(n^2)
    hashTable, truckList = delivery()

    # Complexity:
    # Space/Time: O(n)
    # Loop until user is satisfied
    ui(hashTable, truckList)
