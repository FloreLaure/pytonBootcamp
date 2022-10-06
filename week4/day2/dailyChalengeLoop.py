
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
newchaine=""
for i in chaine:
    if i not in newchaine:
        newchaine +=i
print(newchaine)