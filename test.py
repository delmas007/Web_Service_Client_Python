import zeep

wsdl_url = "http://localhost:8084/Operatione?wsdl"

client = zeep.Client(wsdl=wsdl_url)
result = client.service.addition(3,4)

print(""" 
    Bienvenu(e) au Menu:
    \n 1-Addition
    \n 2-Division
    \n 3-Nombre premier
    \n 0-Quitter
    """)
choix = int(input("Votre choix :"))

while choix != 0:
    if choix == 1 :
        a = float(input("premier chiffre :"))
        b = float(input("deuxieme chiffre :"))
        result = client.service.addition(a,b)
        print(f"{a} + {b} = {result}")
        choix=9
    elif choix == 2 :
        a = float(input("premier chiffre :"))
        b = float(input("deuxieme chiffre :"))
        result = client.service.division(a,b)
        print(f"{a} / {b} = {result}")
        choix=9
    elif choix == 3 :
        a = float(input("chiffre :"))
        result = client.service.premier(a)
        print(result)
        choix=9
    else:
        print("Choix invalide. Veuillez réessayer.")
        print(""" 
            Bienvenu(e) au Menu:
            \n 1-Addition
            \n 2-Division
            \n 3-Nombre premier
            \n 0-Quitter
            """)
    choix = int(input("Votre choix :"))
print('Merci ("_")')