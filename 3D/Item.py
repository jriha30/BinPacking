from copy import deepcopy, copy

class Item:
    def __init__(self, l, w, h, ItemNumber=0, BinNumber=0):
        self.ItemNumber = ItemNumber
        self.BinNumber = BinNumber
        self.length = l
        self.width = w
        self.height = h
        self.OLength = self.length
        self.OWidth = self.width
        self.OHeight = self.height
        self.volume = l * w * h
        self.CurrentCoords = []
        self.ListOfValues = []
    
    def Describe(self):
        print("Dimensions of Item " + str(self.ItemNumber) + ": " + str(self.length) + " x " + str(self.width) + " x " + str(self.height) + " = " + str(self.volume))


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
            self.height = self.OHeight
        elif(RotateCode == 1):
            self.length = self.OLength
            self.width = self.OHeight
            self.height = self.OWidth
        elif(RotateCode == 2):
            self.length = self.OWidth
            self.width = self.OLength
            self.height = self.OHeight
        elif(RotateCode == 3):
            self.length = self.OWidth
            self.width = self.OHeight
            self.height = self.OLength
        elif(RotateCode == 4):
            self.length = self.OHeight
            self.width = self.OLength
            self.height = self.OWidth
        elif(RotateCode == 5):
            self.length = self.OHeight
            self.width = self.OWidth
            self.height = self.OLength

    def GetCoords(self, i, j, k):
        self.CurrentCoords = []
        self.CurrentCoords.append([i,j,k])

        if(self.length - 1 != 0):
            TempList = self.CurrentCoords.copy()
            for i in TempList:
                self.PlaceItemHelperLength(self.length,i[0],i[1],i[2])
        if(self.width - 1 != 0):
            TempList = self.CurrentCoords.copy()
            for i in TempList:
                self.PlaceItemHelperWidth(self.width,i[0],i[1],i[2])
        if(self.height - 1 != 0):
            TempList = self.CurrentCoords.copy()
            for i in TempList:
                self.PlaceItemHelperHeight(self.height,i[0],i[1],i[2])

    def PlaceItemHelperLength(self, length, i,j,k):
        for l in range(1, length):
            self.CurrentCoords.append([i,j+l,k])
    
    def PlaceItemHelperWidth(self, width, i,j,k):
        for l in range(1, width):
            self.CurrentCoords.append([i+l,j,k])

    def PlaceItemHelperHeight(self, height, i,j,k):
        for l in range(1, height):
            self.CurrentCoords.append([i,j,k+l])
    
    def GetAllValues(self, BinList):
        self.ListOfValues = []
        for bin in BinList:
            for i in range(bin.length):
                for j in range(bin.width):
                    for k in range(bin.height):
                        for RotationValue in range(6):
                            temp = []
                            temp.append([i,j,k])
                            temp.append(RotationValue)
                            self.Rotate(RotationValue)
                            self.GetCoords(i,j,k)
                            temp.append(self.CurrentCoords)
                            temp.append(bin.IsValidLocation(self.CurrentCoords))
                            temp.append(bin)
                            self.ListOfValues.append(temp)

    def ChooseLocation(self):
        for location in self.ListOfValues:
            if(location[3]):
                self.CurrentCoords = location[2]
                return True, location
        return False, location