birthdays = {
    "Severine" : "1998/12/26",
    "Larissa" : "2002/08/03",
    "Tatiana" : "2002/11/07",
    "Madeleine" : "2003/10/10",
    "Laure" : "2001/01/08"
}
#Exercice 1 
print("\nWelcome, You can look up the birthdays "
      "of the people in the list\n")
nom = input("Entrez le nom d'une personne : ")
date = birthdays[nom.lower()]
print("La date d'anniversaire de :",nom,"est",date)

#Exercice 2 
for x in birthdays :
    print(x)

nom = input("Entrez le nom d'une personne : ")
if nom not in birthdays :
    print("nous n'avons pas les informations d'anniversaire pour ",nom)
else :
    date = birthdays[nom.lower()]
    print("La date d'anniversaire de :", nom, "est", date)

#Exercice 3 
nomPer = input("Entrez le nom d'une personne : ")
print("Entrez la date de naissance de :",nomPer, "au format YYYY/MM/DD")
datePer = input()
birthdays[nomPer] = datePer
for x in birthdays :
    print(x)

#Exercice 4 
#1
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
phrases = "On a:"
for x in items :
    phrases += "\n"+x+" avec pour prix "+str(items[x])
print(str(phrases))
#2
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
prix = 0
for x in items :
    prix += items[x]["price"]*items[x]["stock"]
print(prix)