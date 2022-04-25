import Functions

bin1,ItemList1 = Functions.Scenario(1)
bin2,ItemList2 = Functions.Scenario(2)
bin3,ItemList3 = Functions.Scenario(3)

def Scenario(ItemList):
    print("You will need " + str(len(ItemList)) + " boxes for " + str(len(ItemList)) + " items.")


def main():
    Scenario(ItemList1)
    Scenario(ItemList2)
    Scenario(ItemList3)

main()