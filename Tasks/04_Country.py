# List items are ordered, changeable, and allow duplicate values.
myFirstList = ["Magyarország", "Litvánia", "USA","Oroszország"];

print(myFirstList)

print ("=====")
for x in myFirstList:
    if (x.find("ország") > 0):
        print(x)