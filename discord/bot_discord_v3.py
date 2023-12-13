#exercice 1

def longueur_chaine(ch):
    return(len(ch))

#ex 2

a = input("chaine de caractere fdp : ")
p=input("la caractere qui se repete mange merde : ")
j=0
for i in a:
    if i==p:
        j+=1
print(j)

#ex 3

def est_chiffres(chaine):
    for caractere in chaine:
        if not caractere.isdigit():
            return False
    return True

chaine = input("Entrez une chaîne de caractères : ")
resultat = est_chiffres(chaine)
print(resultat)

#ex 4

def supprimer_espaces(ch):
    return ch.replace(" ", "")

ch = input("Entrez une chaîne de caractères : ")
resultat = supprimer_espaces(ch)
print(resultat)
