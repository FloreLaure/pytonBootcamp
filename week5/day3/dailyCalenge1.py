class cercle:
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        import math
        return math.pi * self.radius

    def __str__(self):
        return "Super"

    def __add__(self, other):
        return self.radius + other.radius

    def comp(self, other):
        if self.radius < other.radius :
            return f"Le cercle de rayon {other.radius} est le plus grand."
        elif self.radius > other.radius :
            return f"Le cercle de rayon {self.radius} est le plus grand."
        return "Egalité"

    def egal(self, other):
        if self.radius == other.radius:
            return True
        return False

    def trie(self,*args):
        tab = []
        for x in args:
            tab.append(x)
        for i in range(0,len(tab)):
            tmp = tab[i]
            j=i-1
            while j>=0 and tab[j].radius > tmp.radius:
                tab[j+1] = tab[j]
                j=j-1
            tab[j+1] = tmp
            print(tab)
        return tab

boite = cercle(5)
lol  = cercle(51)
lol1  = cercle(15)
lol2  = cercle(115)
lol3  = cercle(511)
lol4  = cercle(50)
print(boite)
print(boite.aire())
print(boite.comp(lol))
print(boite.egal(lol))
tab = boite.trie(lol,lol1,lol2,lol3,lol4)
for x in tab :
    print(x.radius)