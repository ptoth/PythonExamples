szoveg = "Python" + "Scripts"
print(szoveg)   

szoveg2 = " are the best!"
szoveg = "Python" + "Scripts" + szoveg2

szoveg = "Python"
print(len(szoveg))

szoveg = "NégyszögletűKerekerdő"

print("4-10. karakter, 2-es lépésközzel:", szoveg[4:10:2])  
print("2-5. karakter:", szoveg[2:5])
print("Elejétől a 6. karakterig:", szoveg[:6])
print("6. karaktertől a string végéig:", szoveg[6:])
print("A teljes szöveg:", szoveg[:])
print("Minden második karakter:", szoveg[::2])

szoveg = "Géza kék az ég"
print(szoveg[::-1]) 

"""
s.lower(): csupa kisbetűssé alakítja az s stringet
s.upper(): csupa nagybetűssé alakítja az s stringet
s.startswith(v): igazat ad vissza, ha az s string a v értékkel kezdődik
s.endswith(v): igazat ad vissza, ha az s string a v értékre végződik
s.count(v): visszaadja, hogy az s stringben hányszor szerepel a v érték
s.strip(): eltávolítja az s string elején és végén lévő helyközöket
s.lstrip(): csak az s string elején lévő helyközöket távolítja el (left strip)
s.rstrip(): csak az s string végén lévő helyközöket távolítja el (right strip)
s.replace(old, new): lecseréli az s stringben az összes old részstringet new-ra
s.split(delim): feldarabolja az s stringet delim karakterek mentén (listát ad vissza)
s.isalpha(): igazat ad vissza, ha az s stringben csak betűk szerepelnek
s.isdigit(): igazat ad vissza, ha az s stringben csak számjegyek szerepelnek
"""

szoveg = "   The red fox jumps over the lazy dog                "
szoveg = szoveg.strip()   # helyközök eltávolítása a szöveg elejéről és végéről

print(szoveg.lower())               # kisbetűsítés
print(szoveg.upper())               # nagybetűsítés
print(szoveg.endswith("szerint"))   # a "szerint" stringre végződik-e a szöveg
print(szoveg.count("a"))            # hány darab 'a' betű van a szövegben
print(szoveg.replace("szalonna", "kolbász"))  # lecserélés
print(szoveg.split(" "))            # feldarabolás szóközök mentén

