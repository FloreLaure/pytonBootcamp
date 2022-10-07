#Exercice 1 
#1
mark = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
#2
mark = mark.split(", ")
#3
print("Le nombre de fabricants est : ",len(mark))
#4
mark.sort( reverse = True)
print(mark)
#5
nbr = 0
for x in mark :
    if "o" in x :
        nbr += 1
print("Il ya ",nbr,"les noms de fabricants qui contiennent la lettre 'o'")
nbr = 0
for x in mark :
    if "i" not in x :
        nbr += 1
print("Nous avon ",nbr,"noms de fabricants qui ne contiennent pas la lettre 'i'")
#6
mark = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
mark = list(set(mark))
n_mark = ""
for x in range(0,len(mark)) :
    if x == len(mark)-1 :
        n_mark += mark[x]
    else :
        n_mark += mark[x] + ", "
print(n_mark)

#7
mark.sort()
n_mark = ""
for x in mark :
    list(x)
    mot = ""
    for i in range((len(x)-1),-1,-1) :
        mot += x[i]
    n_mark += mot + "\n"
print(n_mark)