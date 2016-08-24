choice = input("Would you like to: \n (S)tart \n (Q)uit").upper()

if choice != "Q":
    x = int(input("Enter the value for x: "))
    y = int(input("Enter the value for y: "))
    evenList = [i for i in range(x,y) if i % 2 == 0]
    print(evenList)
    oddList = [i for i in range(x, y) if i % 2 != 0]
    print(oddList)
    squares = [i ** 2 for i in range(x,y)]
    print(squares)
