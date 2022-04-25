import Item
import Bin
from random import randint, shuffle
from copy import deepcopy

def GenerateRandomItem(Length, Width, Height):
    return Item.Item(randint(1,Length), randint(1,Width), randint(1,Height))

def CreateTestItem(Length=1, Width=1, Height=1):
    return Item.Item(Length, Width, Height)

def GenerateRandomBin(Length=10, Width=10, Height=10):
    return Bin.Bin(randint(1,Length), randint(1,Width), randint(1,Height))

def CreateContainer(Length, Width, Height):
    return Bin.Bin(Length, Width, Height)

def CloseBin(bin):
    print("\nBin number " + str(bin.BinNumber) + " is closed")
    print("Space Remaining in bin: " + str(bin.SpaceAvailable) + "\n")

def EndingLog(Bin, ListOfBins, ItemList):
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!  " + "FINAL REPORT" + "  !!!!!!!!!!!!!!!!!!!!!!!!")
    TotalSpace = Bin.volume * len(ListOfBins)
    OpenSpace = 0
    for Bin in ListOfBins:
        OpenSpace += Bin.SpaceAvailable
    FilledSpace = TotalSpace - OpenSpace
    print()
    for bin in ListOfBins:
        bin.DisplayVolume()
    print("Boxes Used: " + str(len(ListOfBins)))
    print("Items Placed: " + str(len(ItemList)))
    print("Open Space: " + str(OpenSpace))
    print("Filled Space: " + str(FilledSpace))
    print("Total Space: " + str(TotalSpace) + "\n")

def Logging(item, bin):
    item.Describe()
    bin.DisplayVolume()

def Scenario(Value):
    bin = Bin.Bin(12,9,6)
    ItemList = []
    ItemA = Item.Item(5,4,3)
    ItemB = Item.Item(3,3,3)
    ItemC = Item.Item(6,2,2)
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
    return bin, ItemList

def DefinedScenario(Size, ItemNumber):
    bin = Bin.Bin(Size,Size,Size)
    ItemList = []
    for i in range(ItemNumber):
        ItemList.append(GenerateRandomItem(Size,Size,Size))
    return bin, ItemList

def GetValue(Value, Size, ItemNumber):
    if(Value == 0):
        Bin, ListOfItems = DefinedScenario(Size, ItemNumber)
    else:
        Bin, ListOfItems = Scenario(Value)

    shuffle(ListOfItems)
    for i in range(len(ListOfItems)):
        ListOfItems[i].ItemNumber = i + 11

    return Bin, ListOfItems

def DescribeListOfItems(ListOfItems):
    for item in ListOfItems:
        item.Describe()

def DoScenario(Value, Size=10, ItemNumber=30):
    Bin, ListOfItems = GetValue(Value, Size, ItemNumber)

    DescribeListOfItems(ListOfItems)

    ListOfBins = []
    ListOfBins.append(deepcopy(Bin))
    BinCounter = 0
    CurrentBin = ListOfBins[BinCounter]
    CurrentBin.BinNumber = BinCounter
    i = 0
    while(i < len(ListOfItems)):
        ListOfItems[i].GetAllValues(CurrentBin)
        # Logging(ListOfItems[i], CurrentBin)
        if(ListOfItems[i].ChooseLocation()):
            CurrentBin.PlaceItem(ListOfItems[i])
            i += 1
        else:
            CloseBin(CurrentBin)
            ListOfBins.append(deepcopy(Bin))
            BinCounter += 1
            CurrentBin = ListOfBins[BinCounter]
            CurrentBin.BinNumber = BinCounter
    EndingLog(Bin, ListOfBins, ListOfItems)