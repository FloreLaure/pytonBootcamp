# Exercice 1 
#2
class Info:
    def __init__(self):
        #1
        print(abs(4.5))
        print(int("7"))
        print(input('Appuyer sur Entrer'))

    def __doc__(self):
        return "Ce programme permet d'imprime des résultats"

info = Info()
print(info.__doc__())

# Exercice 2 
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __repr__(self):
        if self.amount > 1 :
            return f"{self.amount} {self.currency}s"
        else :
            return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        a=True
        try :
            if self.currency == other.currency :
                print(self.amount + other.amount)
                return Currency(self.currency,self.amount + other.amount)
            else :
                a=False
        except :
            if a :
                print(self.amount + other)
                return Currency(self.currency,self.amount + other)
        if not a :
            raise TypeError("Impossible d'ajouter entre le type de devise <dollar> et <shekel>")




c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))

print(int(c1))

print(repr(c1))

c1 + 5

c1 + c2

print(c1)

c1 += 5

print(c1)

c1 += c2

print(c1)