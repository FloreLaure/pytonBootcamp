mot = input("Entrez une sentense : ")
mot = mot.split(" ")
sentense = ""
for x in range(len(mot)-1,-1,-1) :
    sentense += mot[x] + " "
    print(x)
print(sentense)