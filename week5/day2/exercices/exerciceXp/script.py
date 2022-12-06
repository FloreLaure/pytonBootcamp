# Exercice 3 
from main import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(f"{self.bark()}")

    def play(self, *args):
        mot = self.name + ", "
        for i in range(0, len(args)):
            if i == len(args) - 1:
                mot += args[i]
            elif i == len(args) - 2:
                mot += args[i] + " et "
            else:
                mot += args[i] + ", "
        print(f"{mot}, all play together")

    def do_a_trick(self):
        import random
        if self.trained == True:
            alea = random.randint(1, 4)
            if alea == 1:
                print(f"{self.name} fait un tonneau")
            elif alea == 2:
                print(f"{self.name} se dresse sur ses pattes arrière")
            elif alea == 3:
                print(f"{self.name} te serre la main")
            else:
                print(f"{self.name} fait le mort")
        else :
            print("It can't")

print("\n")
dog1 = PetDog('sifu', 1, 30, False)
dog2 = PetDog('rufus', 5, 25, True)
dog3 = PetDog('triou', 10, 40, True)

dog1.train()
dog2.play(dog1.name,dog2.name)
dog3.do_a_trick()
dog3.do_a_trick()
dog1.do_a_trick()