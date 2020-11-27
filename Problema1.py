sir=str(input("Dati un sir de caractere: "))
majuscule=0
cifre=0
caractere_speciale=0
for i in range(0,len(sir)):
    if(((ord(sir[i])>=48)and(ord(sir[i])<=57))):
        cifre+=1
    elif((ord(sir[i])>=65)and(ord(sir[i])<=90)):
        majuscule+=1
    elif(((ord(sir[i])>=33)and(ord(sir[i])<=47))or((ord(sir[i])>=58)and(ord(sir[i])<=64))or((ord(sir[i])>=90)and(ord(sir[i])<=96))or((ord(sir[i])>=123)and(ord(sir[i])<=127))):
        caractere_speciale+=1
print("Numarul de majuscule este",majuscule)
print("Numarul de cifre este",cifre)
print("Numarul de caractere speciale este",caractere_speciale)