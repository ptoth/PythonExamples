numOfGuests = int(input(("Please provide, how many guests you are expecting:")))
guestList = []

menuIndex = -1
while menuIndex != 9:
    print("========================================")
    print("Please choose from the menu:")
    print("1. add guest to the end of the list")
    print("2. remove guest")
    print("3. list guests in order of addition")
    print("4. list guests in alphabetical order")
    print("9. exit")
    menuIndex = int(input("Input: "))

    if menuIndex == 1:
        newGuest = input("Please provide the guest' name: ")
        guestList.append(newGuest)

    if menuIndex == 3:
        if guestList:
            print(guestList)
        else:
            print("The list is empty!")
        
    if menuIndex == 4:
        # To avoid permanent change, using sorted
        print(sorted(guestList))
    
    if menuIndex == 5:
        pass
