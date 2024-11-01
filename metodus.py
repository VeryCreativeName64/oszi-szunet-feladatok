def elso_feladat():
    szam=int(input("Kérek egy egész számot 200 és 920 között: "))
    while (szam<200 or szam>920):
        szam:int=int(input("Mondom 200 és 920 között kérek egész számot: "))
    if (szam>=200 and szam<=920):
        print(f"Az általad megadott érték első számjegye: {str(szam)[0]}")

def feladat_2(szam):
    if(szam==0):
        print("Be se jövünk!")
    elif(szam==1):
        print(f"Még 90% on vagyunk!")
    elif(szam==2 or szam==3):
        print(f"Még bírjuk (60%)")
    elif(szam>=4 and szam<=7):
        print(f"Progit tanulunk, töltődünk! 70%")
    elif(szam==8 or szam==9):
        print(f"Lassan nem bírjuk tovább! 50%")
    elif(szam<=10):
        print(f"Ez már tényleg túlzás.")

def feladat_4():
    import math
    szam = float(input("Adj meg egy számot: "))
    while(szam<0):
        szam = float(input("Hiba: a szám nem lehet negatív, próbáld újra: "))
    if(szam>=0):
        negyzetgyok = math.sqrt(szam)
        print(f"A {szam} négyzetgyöke: {negyzetgyok}")

def feladat_5():
    szam1 = float(input("Add meg a téglalap egyik oldalát: "))
    szam2 = float(input("Add meg a téglalap másik oldalát: "))
    while(szam1<=0 or szam2<=0):
        if(szam1==0 or szam1<=0):
            szam1 = float(input("Hiba: az egyik oldal negatív, próbáld újra: "))
        if(szam2==0 or szam2<=0):
            szam2 = float(input("Hiba: a másik oldal negatív, próbáld újra:  "))
    if(szam1>0 and szam2>0):
        szamosszeg=szam1+szam2
        terulet=szam1*szam2
        kerulet=2*szamosszeg
        print(f"a téglalap területe: {terulet:.2f}")
        print(f"a téglalap kerülete: {kerulet:.2f}")

def feladat_6():
    lista=["A","B","C","D","E","F","G","H"]
    szektor = input("Add meg a szektor nagy betűjelét Atól H-ig, és megmutatom, mi található ott: ").upper()
    while szektor not in lista:
          szektor = input("Hiba: ilyen szektor nincs, próbáld újra: ").upper()
    if szektor == "A":
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif szektor == "B" or szektor == "E":
        print("Kereskedelmi Csarnok")
    elif szektor == "C":
        print("Konferencia-központ Innovációs Showroom")
    elif szektor == "D":
        print("Hal, Víz és Ember")
    elif szektor == "F":
        print("Hagyományos Vadászati Módok Csarnoka")
    elif szektor == "G":
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21. században kiállítás")
    elif szektor == "H":
        print("Központi Magyar Kiállítás")
    



    


