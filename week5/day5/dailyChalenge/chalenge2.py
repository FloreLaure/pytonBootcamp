


# Partie 2 : 
class Card:
    def __init__(self,couleur,valeur):
        self.couleur = couleur
        self.valeur = valeur

class Deck:
    def shuffle(self,tab):
        import random
        tab1 = []
        taille = 51
        for x in range(0,52):
            tab1.append(tab.pop(random.randint(0,taille)))
            taille -= 1
        return tab1

    def genCard(self,couleur):
        cardTab = []
        cardTab.append(Card(couleur, "A"))
        cardTab.append(Card(couleur, "J"))
        cardTab.append(Card(couleur, "Q"))
        cardTab.append(Card(couleur, "K"))
        for i in range(2,11):
            cardTab.append(Card(couleur, i))
        return cardTab

    def deal(self,tab):
        return tab.pop()

a = Deck()
pack = a.genCard("Hearts")
pack += a.genCard("Diamonds")
pack += a.genCard("Clubs")
pack += a.genCard("Spades")

for x in pack:
    print(x.couleur,x.valeur)
print()

pack = a.shuffle(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()

user = a.deal(pack)

for x in pack:
    print(x.couleur,x.valeur)
print()










