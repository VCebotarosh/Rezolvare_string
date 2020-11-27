cuvant1=str(input("Dati un cuvant: "))
cuvant2=str(input("Dati al doilea cuvant: "))
cuvant3=str(input("Dati al treilea cuvant: "))
cuvant4=str(input("Dati al patrulea cuvant: "))
if((len(cuvant1)>=3)and(len(cuvant2)>=3)and(len(cuvant3)>=3)and(len(cuvant4)>=3)):
    print(cuvant1)
    print(cuvant2)
    print(cuvant3)
    print(cuvant4)
    i=len(cuvant4)//2
    print(cuvant1[:2]+cuvant2[0]+cuvant3[:3]+cuvant4[0:i])
else:
    print("Ati introdus datele gresit")