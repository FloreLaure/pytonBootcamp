# Exercice 1 
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1
class Siamese(Cat) :
    def sing(self, sounds):
        return f'{sounds}'

#2
all_cats = [Bengal('sifu',2),Chartreux('rufus',5),Siamese('triou',10)]

#3
sara_pets = Pets(all_cats)

#4
sara_pets.walk()



# Exercice 2 

class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight/(self.age*10)

    def fight(self,other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f'{self.name} is a winner')
        else :
            print(f'{other_dog.name} is a winner')

#3
dog1 = Dog('sifu',1,30)
dog2 = Dog('rufus',5,25)
dog3 = Dog('triou',10,40)

print(f'{dog1.run_speed()} m/s.')
dog2.fight(dog3)
