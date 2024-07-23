class Package:
    def __init__(self, ID, address, city, state, zCode, deadline, weight, notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zCode = zCode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self): # Overwrites print(Package). Otherwise, it will print out the object reference.
        return f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zCode}, {self.deadline}, {self.weight}, {self.notes}"
