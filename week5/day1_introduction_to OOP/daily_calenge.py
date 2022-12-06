# Mode D'emploi : Ancienne Ferme MacDonald
class Farm:
    def __init__(self, name):
        self.name = name
        self.animal = {}

    def add_animal(self, name, nombre=1):
        if name in self.animal :
            self.animal.update({name : self.animal[name]+nombre})
        else :
            self.animal.update({name : nombre})

    def get_info(self) :
        mot = ""
        print(f"{self.name}'s farm\n")
        for x in self.animal :
            mot += x + " : " + str(self.animal[x]) + "\n"
        mot += "\n\tE-I-E-I-0!"
        return mot

    def get_animal_types(self) :
        animal = []
        for x in self.animal :
            animal.append(x)
        return sorted(animal)

    def get_sort_info(self) :
        mot = "\nMcDonald’s farm has "
        animal = self.get_animal_types()
        for i in range(0,len(animal)) :
            if i == len(animal)-1 :
                mot += animal[i] + "."
            elif i == len(animal)-2 :
                mot += animal[i] + " and "
            else :
                mot += animal[i] + ", "
        return mot


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_sort_info())