
##  chalenge1
a = int(input("entrez un nombre"))
b = int(input("entrez une taille"))
multipl = 0
lis = []
while b>0:
	multipl = a + multipl
	lis.append(multipl)
	b = b - 1 
print(lis)

##  chalenge2

chaine=input("entrez une chaine de caratere")
for i in range(len(chaine) - 1):
    if chaine[i + 1] == chaine[i] + 1:
        chaine.remove(chaine[i+1])
print(chaine)