# Partie 1
class Text:
    def __init__(self, chaine):
        self.chaine = chaine.split(" ")

    def frequent(self, mot):
        return self.chaine.count(mot)

    def plusFrequentuent(self):
        mot = {}
        grand = ""
        for x in self.chaine :
            if x not in mot and mot != {}:
                mot.update({x : self.frequent(x)})
                if mot[grand] < mot[x]:
                    grand = x
            elif mot == {}:
                mot.update({x: self.frequent(x)})
                grand = x
        return grand

    def unique(self):
        return list(set(self.chaine))

    # Partie 2
    def from_file(self, nomFic):
        text = ""
        with open(nomFic, "r") as f :
            for x in f :
                text += x[0:len(x)-1]
        return text

a= Text("Un bon livre coûterait maison parfois autant qu'une bonne 1 1 1 1 1 parfois parfois maisonparfois")
print(f"Ce mot apparait {a.frequent('parfois')} fois")
print(f"Le mot le plus courant est {a.plusFrequent()}")
print(f"liste des éléments unique {a.unique()}")

b = Text(a.from_file('the_stranger.txt'))
print(f"\nCe mot apparait {b.frequent('the')} fois")
print(f"Le mot le plus courant est {b.plusFrequent()}")
print(f"liste des éléments unique {b.unique()}")