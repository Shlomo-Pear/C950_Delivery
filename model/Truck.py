class Truck:
    def __init__(self, ID, capacity=16, timeLeft="8:00"):
        self.ID = ID
        self.capacity = capacity
        self.packages = []
        self.timeLeft = timeLeft
        self.miles = 0.0

