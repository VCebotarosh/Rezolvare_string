CNP=str(input("Dati CNP-ul unei persoane: "))
cifra_corecta=0
if(len(CNP)==13):
    for i in range(0,len(CNP)):
        if((ord(CNP[i])>=48)and(ord(CNP[i])<=57)):
            cifra_corecta+=1
    if(cifra_corecta==13):
        print("CNP-ul este corect")
    else:
        print("CNP-ul nu este valid")
else:
    print("CNP-ul nu este valid")