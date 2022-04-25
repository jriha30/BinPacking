import Functions
from copy import deepcopy

def main():
    ListOfBins = []
    # Bin, ListOfItems = Functions.Scenario(2)
    Bin, ListOfItems = Functions.DefinedScenario(3,2)
    ListOfBins.append(deepcopy(Bin))
    BinCounter = 0

    CurrentBin = ListOfBins[BinCounter]
    CurrentBin.BinNumber = BinCounter + 1

    i = 0
    while(i < len(ListOfItems)):
        ListOfItems[i].GetAllValues(CurrentBin)
        # Functions.Logging(ListOfItems[i], CurrentBin)
        if(ListOfItems[i].ChooseLocation()):
            CurrentBin.PlaceItem(ListOfItems[i])
            i += 1
        else:
            Functions.CloseBin(CurrentBin, len(ListOfBins))
            ListOfBins.append(deepcopy(Bin))
            BinCounter += 1
            CurrentBin = ListOfBins[BinCounter]

    Functions.EndingLog(Bin, ListOfBins, ListOfItems)

main()