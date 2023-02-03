# Exercice 1 : Importer
from func import addition as a
print(a(5,5))

#Exercice 2 : Module Aléatoire
def alea (num1) :
    import random as r
    if num1 in range(0,101):
        if num1 == r.randint(0,100):
            print("Super")
alea(5)

# Exercice 3 : Module Cordes
import random as r
import string

mot = "".join([r.choice(string.ascii_letters) for i in range(0,5)])

print(mot)



# Exercice 4 : Date 
def actu():
    from datetime import datetime, time
    print(datetime.now())

#Exercice 5 : 
def timeRest():
    import datetime
    janv = "01/01/2023"
    janv = datetime.datetime.strptime(janv, "%d/%m/%Y")
    rest = janv-datetime.datetime.now()
    rest1= str(rest)
    print(f"il reste {rest.days} et {rest1[len(rest1)-14:len(rest1)-7]} heures")

timeRest()

# Exercice 6 : 
def vie():
    import datetime
    anniv = input("Entrez votre date d'anniversaire en respectant le format DD/MM/YYYY : ")
    anniv = datetime.datetime.strptime(anniv, "%d/%m/%Y")
    minute = datetime.datetime.now() - anniv
    print(f"Vous avez {int(minute.total_seconds()/60)} minutes de vie")

vie()

# Exercice 7 : 
def dateJour():
    import datetime
    print(datetime.datetime.now())
    vac = "25/12/2022"
    vac = datetime.datetime.strptime(vac, "%d/%m/%Y")
    rest = vac-datetime.datetime.now()
    rest1 = str(rest)
    print(f"il reste {rest.days} et {rest1[len(rest1)-14:len(rest1)-7]} heures pour la noël")

dateJour()

# Exercice 8 : 
def ageSec():
    ageS = 1000000000
    print(f"Vous avez sur terre : {ageS/31557600} ans.")
    print(f"Vous avez sur Mercure  : {ageS/(31557600 * 0.2408467)} ans.")
    print(f"Vous avez sur Vénus   : {ageS/(31557600 * 0.61519726)} ans.")
    print(f"Vous avez sur Mars    : {ageS/(31557600 * 1.8808158)} ans.")
    print(f"Vous avez sur Jupiter     : {ageS/(31557600 * 11.862615)} ans.")
    print(f"Vous avez sur Mars    : {ageS/(31557600 * 29.447498)} ans.")
    print(f"Vous avez sur Uranus    : {ageS/(31557600 * 84.016846)} ans.")
    print(f"Vous avez sur Neptune     : {ageS/(31557600 * 164.79132)} ans.")

ageSec()


# Exercice 9 : 
users = []
def modFaker(users):
    from faker import Faker
    faker = Faker()
    langue = ['fr','en','aa','af']
    lang = str(faker.sentence(ext_word_list = langue)).split(" ")
    users.append({'nom': faker.name(),'adresse': faker.address(), 'code_langue': lang[0]})

modFaker(users)
modFaker(users)
modFaker(users)
modFaker(users)
print(users)



def addition(a,b):
    return a+b