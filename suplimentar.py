sir=str(input("Dati un sir : "))
i=0
if(len(sir)<=50):
    while(len(sir)>=1):
        print(i*" "+sir)
        sir=sir[1:(len(sir)-1)]
        i+=1
else:
    print("Ati introdus datele gresit")