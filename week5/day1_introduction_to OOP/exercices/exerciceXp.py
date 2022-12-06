class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("miaou",3)  
cat2 = Cat("loulou",5) 
cat3 = Cat("mia",1) 
   
def ancien(): 
	maxi=max([cat1.age,cat2.age,cat3.age])
	print("le chat le plus agée est ", ,"il a ",maxi, " age") 

ancien()





# Exercice 1 : Chats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
chat = []
chat.append(Cat("youuga",3))
chat.append(Cat("krikri",5))
chat.append(Cat("yosa",10))

def catAge (chats):
    chat = chats[0]
    for x in chats :
        if x.age > chat.age :
            chat = x
    return chat
chatA = catAge(chat)
print(f"The oldest cat is {chatA.name}, and is {chatA.age} years old.")

#Exercice 2 : Chiens
#1...4
class Dog :
    def __init__(self, name, height) :
        self.name = name
        self.height = height

    def bark(self) :
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jump {self.height*2} cm high!")
#5...6
davids_dog = Dog("Rex",50)
print(f"Chien de David: {davids_dog.name} and have {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()
print("\n")
#7...8
sarahs_dog = Dog("Teacup", 20)
print(f"Chien de Sarah: {sarahs_dog.name} and have {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()
#9
print("\n")
if sarahs_dog.height > davids_dog.height:
    print(f"Chien de Sarah: {sarahs_dog.name}")
else:
    print(f"Chien de David: {davids_dog.name}")

#Exercice 3 : Qui Est Le Producteur De La Chanson ?
class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        list(map(lambda x : print(x),self.lyrics))

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Exercice 4 : Après-Midi Au Zoo
class Zoo :
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        list(map(lambda x : print(x),self.animals))

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        ani = sorted(self.animals)
        animal ={}
        animal.update({1:ani[0]})
        j=2
        for i in range(1,len(ani)) :
            if ani[i][0] == ani[i-1][0] :
                animal.update({j-1: animal[j-1]+[ani[i]]})
            else :
                animal.update({j: [ani[i]]})
                j+=1
        return animal

    def get_groups(self,animal,animaux):
        print(f"{animal}/")
        for x in animaux :
            if animal[0] == animaux[x][0][0] :
                print(f"{animaux[x]}")


ramat_gan_safari = Zoo("sss")

while True :
    ani = input("Which animal should we add to the zoo ? : ")
    if ani.lower() != "exit" :
        ramat_gan_safari.add_animal(ani)
    else:
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

while True :
    ani = input("Which animal should we delete to the zoo ? : ")
    if ani.lower() != "exit" :
        ramat_gan_safari.sell_animal(ani)
    else :
        break
    print("Entrez 'exit' pour quitter")

ramat_gan_safari.get_animals()
print("\n")

animals = ramat_gan_safari.sort_animals()
print(animals)
print('\n')

animal = input("Entrez le nom d'un animal existant : ")
ramat_gan_safari.get_groups(animal,animals)

