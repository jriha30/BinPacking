import Item
import Bin
from random import randint, shuffle
from copy import deepcopy

def GenerateRandomItem(Length, Width):
    return Item.Item(randint(1,Length), randint(1,Width))

def CreateTestItem(Length=1, Width=1):
    return Item.Item(Length, Width)

def GenerateRandomBin(Length=10, Width=10):
    return Bin.Bin(randint(1,Length), randint(1,Width))

def CreateContainer(Length, Width):
    return Bin.Bin(Length, Width)

def CloseBin(bin, index):
    print("\nBin number " + str(index) + " is closed")
    print("Space Remaining in bin: " + str(bin.SpaceAvailable) + "\n")

def EndingLog(Bin, ListOfBins, ItemList):
    TotalSpace = Bin.area * len(ListOfBins)
    OpenSpace = 0
    for Bin in ListOfBins:
        OpenSpace += Bin.SpaceAvailable
    FilledSpace = TotalSpace - OpenSpace
    print()
    for bin in ListOfBins:
        bin.DisplayArea()
    print("Boxes Used: " + str(len(ListOfBins)))
    print("Items Placed: " + str(len(ItemList)))
    print("Open Space: " + str(OpenSpace))
    print("Filled Space: " + str(FilledSpace))
    print("Total Space: " + str(TotalSpace) + "\n")

def Logging(item, bin):
    item.Describe()
    bin.DisplayArea()

def Scenario(Value):
    bin = Bin.Bin(12,9)
    ItemList = []
    ItemA = Item.Item(5,4)
    ItemB = Item.Item(3,3)
    ItemC = Item.Item(6,2)
    if(Value == 1):
        Tuple = [2,6,2]
    elif(Value == 2):
        Tuple = [5,10,5]
    elif(Value == 3):
        Tuple = [12,12,6]
    for i in range(Tuple[0]):
        ItemList.append(deepcopy(ItemA))
    for i in range(Tuple[1]):
        ItemList.append(deepcopy(ItemB))
    for i in range(Tuple[2]):
        ItemList.append(deepcopy(ItemC))
    for i in range(len(ItemList)):
        ItemList[i].ItemNumber = i + 1
    shuffle(ItemList)
    return bin, ItemList

def DefinedScenario(Size, ItemNumber):
    bin = Bin.Bin(Size,Size)
    ItemList = []
    for i in range(ItemNumber):
        ItemList.append(CreateTestItem())
    for i in range(len(ItemList)):
        ItemList[i].ItemNumber = i + 1
    shuffle(ItemList)
    return bin, ItemList