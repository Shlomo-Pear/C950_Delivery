# Shlomo Pear 001504646
"""
Mailing system program that loads up trucks with packages, determines the next location to drop off a package, tracks
the delivery statuses (UNKNOWN, AT HUB, EN ROUTE, DELIVERED) of the packages, and updates the package details with truck
number, departure time, and delivery time.
"""

from goMethods.Delivery import *
from goMethods.UI import *


# Ref: WGU Webinar: Python Modules; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a6e33b6d-9753-4ba4-a1b6-ac8000f5d250
if __name__ == '__main__':
    print("WGU Mail Routing System")

    hashTable, truckList, originalPackage = delivery()

    # Loop until user is satisfied
    ui(hashTable, truckList, originalPackage)
