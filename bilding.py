class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
        self.dict = {"north-east": '', "south-east": '', "south-west": '', "north-west": ''}

    def corners(self):
        self.dict["north-east"] = [self.south + self.width_NS, self.west + self.width_WE]
        self.dict["south-east"] = [self.south, self.west + self.width_WE]
        self.dict["south-west"] = [self.south, self.west]
        self.dict["north-west"] = [self.south + self.width_NS, self.west]
        return self.dict

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)

if __name__ == "__main__":
    b = Building(1, 2, 2, 3)
    print(b.volume())