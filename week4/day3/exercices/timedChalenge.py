#Nombre nbParfait
nombre = int(input("Entrez un nombre : "))
nbParfait = 0
for i in range(1,nombre) :
    if nombre%i == 0 :
        nbParfait += i
if nbParfait == nombre :
    print(nombre,"est un nombre nbParfait")
else :
    print(nombre,"n'est pas un nombre nbParfait")