name = input("Please Enter Your Name: ")
choice = input("(H)ello \n" + "(G)oodbye \n" + "(Q)uit \n" + ">>>").upper()

while choice != "Q":
    if choice == "H":
        print("Hello " + str(name))
    elif choice == "G":
        print("Goodbye " + str(name))
    else:
        print("Invalid Option!")
    choice = input("(H)ello \n" + "(G)oodbye \n" + "(Q)uit \n" + ">>>").upper()
print("Finised.")