cuvant=str(input("Dati un cuvant: "))
litera=str(input("Dati cu ce litera trebuie de inlocuit: "))
for i in range(len(cuvant)):
    cuvant_nou=cuvant[:i]+litera+cuvant[i+1:]
    print(cuvant_nou)    