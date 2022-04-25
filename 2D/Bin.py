from numpy import zeros

class Bin:
    def __init__(self, l, w, BinNumber=0):
        self.BinNumber = BinNumber
        self.length = l
        self.width = w
        self.area = l * w
        self.SpaceAvailable = self.area
        self.space = zeros(shape=(self.length, self.width))
        
    def DisplayArea(self):
        print("Dimensions of Bin " + str(self.BinNumber) + ": " + str(self.length) + " x " + str(self.width)  + " = " + str(self.area))
        for i in self.space:
            print(i)
        print("Space Remaining: " + str(self.SpaceAvailable) + "\n")

    def IsValidLocation(self, ListOfCoords):
        try:
            for tuple in ListOfCoords:
                if(self.space[tuple[0]][tuple[1]] == 1):
                    return False
            return True
        except:
            return False
    
    def PlaceItem(self, item):
        for tuple in item.CurrentCoords:
            self.space[tuple[0]][tuple[1]] += 1
        self.SpaceAvailable -= item.area