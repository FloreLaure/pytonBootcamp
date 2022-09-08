

## exercice1

import math

C = 50
H = 30
D = input("Entrer chaîne de nombres séparés par des virgules")
D.split(",")
for i in D:
    j=int(i)
    Q=math.sqrt(((2 * C * j)/H))
    print(Q)


##  exercice2
number= [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
number.sort(reverse = True) 

