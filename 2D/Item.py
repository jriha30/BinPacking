from copy import deepcopy

class Item:
    def __init__(self, l, w, ItemNumber=0, BinNumber=0):
        self.ItemNumber = ItemNumber
        self.BinNumber = BinNumber
        self.length = l
        self.width = w
        self.OLength = self.length
        self.OWidth = self.width
        self.area = l * w
        self.CurrentCoords = []
        self.ListOfValues = []
    
    def Describe(self):
        print("Dimensions of Item " + str(self.ItemNumber) + ": " + str(self.length) + " x " + str(self.width) + " = " + str(self.area))
    
    def DisplayAllValues(self):
        for value in self.ListOfValues:
            print("Location: " + str(value[0]))
            print("Rotation: " + str(value[1]))
            print("Score: " + str(value[3]))
            print()

    def Rotate(self, RotateCode):
        if(RotateCode == 0):
            self.length = self.OLength
            self.width = self.OWidth
        elif(RotateCode == 1):
            self.length = self.OWidth
            self.width = self.OLength

    def GetCoords(self, i, j):
        # tempi = j
        # j = i
        # i = tempi

        self.CurrentCoords = []
        self.CurrentCoords.append([i,j])

        if(self.length - 1 != 0):
            TempList = self.CurrentCoords.copy()
            for i in TempList:
                self.PlaceItemHelperLength(self.length,i[0],i[1])
        if(self.width - 1 != 0):
            TempList = self.CurrentCoords.copy()
            for i in TempList:
                self.PlaceItemHelperWidth(self.width,i[0],i[1])
    
    def PlaceItemHelperLength(self, length, i,j):
        for l in range(1, length):
            self.CurrentCoords.append([i,j+l])
    
    def PlaceItemHelperWidth(self, width, i,j):
        for l in range(1, width):
            self.CurrentCoords.append([i+l,j])
    
    def GetAllValues(self, bin):
        self.ListOfValues = []
        for i in range(bin.length):
            for j in range(bin.width):
                for RotationValue in range(2):
                    temp = []
                    temp.append([j,i])
                    self.Rotate(RotationValue)
                    temp.append(RotationValue)
                    self.GetCoords(j,i)
                    temp.append(self.CurrentCoords)
                    temp.append(bin.IsValidLocation(self.CurrentCoords))
                    self.ListOfValues.append(deepcopy(temp))
    
    def ChooseLocation(self):
        for location in self.ListOfValues:
            if(location[3]):
                self.CurrentCoords = location[2]
                return True
        return False