numOfGuests = int(input(("Please provide, how many guests you are expecting:")))
guestList = []
for i in range(numOfGuests):
    guestList.append(input("Please provide the name of the guest #"+str(i+1)+":"))

menuIndex = -1
while (menuIndex != 9):
    print("Please choose from the menu:")
    print("1. add guest")
    print("2. remove guest")
    print("3. list guests in order of addition")
    print("4. list guests in alphabetical order")
    print("9. exit")
    menuIndex = int(input("Input: "))

    if (menuIndex == 1):
        newGuest = input("Please provide the guest' name: ")
        guestList.append(newGuest)

    if (menuIndex == 3): 
        print(guestList)
        
    if (menuIndex == 4):
        guestList.sort()
        print(guestList)
    