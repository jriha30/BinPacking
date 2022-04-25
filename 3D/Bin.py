from numpy import ones

class Bin:
    def __init__(self, l, w, h, BinNumber=0):
        self.BinNumber = BinNumber
        self.length = l
        self.width = w
        self.height = h
        self.volume = l * w * h
        self.SpaceAvailable = self.volume
        self.space = ones(shape=(self.length, self.width, self.height)) * -1
        
    def DisplayVolume(self):
        print("Dimensions of Bin " + str(self.BinNumber) + ": " + str(self.length) + " x " + str(self.width) + " x " + str(self.height) + " = " + str(self.volume))
        for i in self.space:
            self.DisplayArea(i)
            print()
        print("Space Remaining: " + str(self.SpaceAvailable) + "\n")
    
    def DisplayArea(self, area):
        for i in area:
            print(i, end="")

    def IsValidLocation(self, ListOfCoords):
        try:
            for tuple in ListOfCoords:
                if(self.space[tuple[0]][tuple[1]][tuple[2]] != -1):
                    return False
            return True
        except:
            return False
    
    def PlaceItem(self, item):
        for tuple in item.CurrentCoords:
            self.space[tuple[0]][tuple[1]][tuple[2]] = item.ItemNumber
        self.SpaceAvailable -= item.volume