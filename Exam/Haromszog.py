haromSzogAoldal = input("Adjon meg az 'a' oldal hosszát: ")
haromSzogBoldal = input("Adjon meg az 'b' oldal hosszát: ")
haromSzogColdal = input("Adjon meg az 'c' oldal hosszát: ")

haromSzogAoldal = float(haromSzogAoldal)
haromSzogBoldal = float(haromSzogBoldal)
haromSzogColdal = float(haromSzogColdal)

#háromszög-egyenlőtlenség vizsgálata

if not(
    (haromSzogAoldal + haromSzogBoldal > haromSzogColdal) and
    (haromSzogAoldal + haromSzogColdal > haromSzogBoldal) and
    (haromSzogBoldal + haromSzogColdal > haromSzogAoldal)
):
    print("A háromszög egyenlőtlenség nem teljesül, nincs ilyen háromszög!")
else:
    print("A háromszög létező:")
    kerulet = haromSzogAoldal + haromSzogBoldal + haromSzogColdal
    print("A háromsög kerülete: ",kerulet)
