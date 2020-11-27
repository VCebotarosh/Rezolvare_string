sir_initial=str(input("Dati numele si prenumele dumneavoastra: "))
var1=sir_initial.split()
if((var1[0]==var1[0].title())and(var1[1]==var1[1].title())):
    print("NUmele si prenumele sunt corecte")
else:
    print("NUmele si prenumele nu sunt corecte")