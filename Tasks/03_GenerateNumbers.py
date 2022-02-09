import random

myRandomNumberList = []

for x in range(15):
    myRandomNumberList.append(random.randrange(-50, 50))

for y in myRandomNumberList:
    if (y > 0):
        print(y)