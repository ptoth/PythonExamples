szoveg = "Python" + "Scripts"
print(szoveg)   

szoveg2 = " are the best!"
szoveg = "Python" + "Scripts" + szoveg2

szoveg = "Python"
print(len(szoveg))

szoveg = "NégyszögletűKerekerdő"

print("4-10. char, with step of 2", szoveg[4:10:2])  
print("2-5. char:", szoveg[2:5])
print("From beginning until 6th char:", szoveg[:6])
print("From 6th to end", szoveg[6:])
print("Whole text:", szoveg[:])
print("Every second char:", szoveg[::2])

szoveg = "Géza kék az ég"
print(szoveg[::-1]) 

szoveg = "   The red fox jumps over the lazy dog                "
szoveg = szoveg.strip()

print(szoveg.lower())               
print(szoveg.upper())               
print(szoveg.endswith("szerint"))   
print(szoveg.count("a"))            
print(szoveg.replace("szalonna", "kolbász"))
print(szoveg.split(" "))

