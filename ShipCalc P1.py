def main():
    numberItems = validate(int(input("How many items will you be calculating: ")))
    Total = 0
    while numberItems > 0:
        Cost = int(input("Cost of item: "))
        Total = Total + Cost
        numberItems = numberItems -1

    if Total > 100:
        print("Total Cost: $ " + str(Total*0.9))
    else:
        print("Total cost: $ " + str(Total))


def validate(NumberItems):
    while NumberItems <= 0:
        NumberItems = int(input("How many items will you be calculating: "))
    return NumberItems

main()