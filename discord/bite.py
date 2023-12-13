try :
    nombre = int(input("entrez un nombre : "))
    print(nombre*2)
except ValueError :
    print("ceci n'est pas un nombre")