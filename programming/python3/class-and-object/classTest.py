class CoordinateWithoutComparison:
    def __init__(self, lat, lon): 
        self.lat = lat
        self.lon = lon

class Coordinate:
    def __init__(self, lat, lon): 
        self.lat = lat
        self.lon = lon
    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon

def main():
    c1 = CoordinateWithoutComparison(0,0)
    print(c1 == CoordinateWithoutComparison(0,0))
    c2 = Coordinate(0,0)
    print(c2 == Coordinate(0,0))

if __name__ == "__main__":
    main()