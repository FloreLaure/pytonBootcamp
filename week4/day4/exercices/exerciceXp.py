# Exercice 1 
def afich_message() :
    print("J'apprends à utilisez les fonctions Python")
afich_message()

# Exercice 2 
def book_favorite(title) :
    print(f"One of my favorite books is {title}")
book_favorite("Candide")

#Exercice 3 
def describe_city(city,country = "Burkina Faso") :
    print(f"{city} is in {country}")
describe_city("Ouagadougou")

# Exercice 4 
import random
def aleatoire(number) :
    alea = random.randint(1,100)
    if alea == int(number) :
        print("Success")
    else :
        print("Try again")
    print("Votre nombre :",number)
    print("Nombre aléatoire :",alea)
aleatoire(52)

# Exercice 5 
#1...4
def make_shirt(size = "XL",text = "I love chocolate") :
    print(f"The size of the shirt is {size} and the text is {text}")
#5
make_shirt()
#6
make_shirt("M")
#7
make_shirt("L","SLFK")
#8
make_shirt(size = "S",text = "SLFK")

# Exercice 6 
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names) :
    list(filter(lambda a: print(a),magician_names))
def make_great(liste) :
    for i in range(0,len(liste)):
        liste[i] += " the Great"
make_great(magician_names)
show_magicians(magician_names)

#Exercice 7 

def get_random_temp(saison) :
    import random
    if saison.lower() == "hiver" :
        return random.randint(-10, 16)
    elif saison.lower() == "autonne" :
        return random.randint(10, 25)
    elif saison.lower() == "printemps" :
        return random.randint(0, 15)
    elif saison.lower() == "été" :
        return random.randint(20, 40)
    else :
        print('Error, default = 0')
        return 0

def main() :
    temp = get_random_temp(input("Saisissez une saison : "))
    print(f"The temperature right now is {temp} degrees Celsius")
    if temp < 0 :
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temp < 16 :
        print("Quite chilly! Don’t forget your coat")
    elif temp <= 23 :
        print("The temperature is ideal")
    elif temp < 32 :
        print("You can go to the beach")
    elif temp < 40 :
        print("It's very hot")
    else:
        print("Dangerous")

main()