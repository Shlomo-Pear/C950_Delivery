"""
This is the truck class.
"""
from datetime import timedelta


class Truck:
    def __init__(self, ID, capacity=16):
        self.ID = ID
        self.capacity = capacity
        self.packages = []
        self.timeLeftHub = timedelta()
        self.timeAfterDelivery = timedelta()
        self.miles = 0.0
