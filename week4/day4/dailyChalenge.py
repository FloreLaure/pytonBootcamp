#Defis du jour : Résolution de la matrice
Matrix = [
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ", "#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
]

def read(liste,index,*args):
    return liste[index]
phrase=[]
top = 0
while top < (len(Matrix[0])):
    compteur=0
    for line in Matrix :
        char = read(line,top)
        if char.isalpha() and char !=" ":
            phrase.append(char)
            compteur=0
        elif compteur==0:
            compteur+=1
            phrase.append("")
        elif compteur==1:
            phrase.append(" ")
            compteur+=1
    top +=1
print("".join(phrase))
#Défis terminé avec succès