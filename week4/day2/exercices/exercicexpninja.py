

## exercice1

import math

C = 50
H = 30
D = input("Entrer chaîne de nombres séparés par des virgules")
listes = D.split(",")
print(listes)
for i in listes:
    Q=math.sqrt(((2 * C * int(i))/H))
    print(Q)


##  exercice2
number= [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]

## The list of numbers – printed in a single line

print(*number)

## The list of numbers – sorted in descending order (largest to smallest)

number.sort(reverse = True) 

##  The sum of all the numbers

print(sum(number))


##  A list of all the numbers greater than 50.
sup50=[]
for i in number:
    if i>50:
        sup50.append(i)

print(sup50)  


##  A list of all the numbers smaller than 10.
inf10=[]
for i in number:
    if i<10:
        inf10.append(i)

print(inf10)   


##  A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
caree=[]
for i in number:
    caree.append(i*i)

print(caree) 


##  The numbers without any duplicates – also print how many numbers are in the new list.
newList=list(set(number))
print(newList)

numbrNum=len(list(set(number)))
print(numbrNum)


##  The average of all the numbers.

print("la moyenne de la nouvelle liste est ",(sum(newList)/numbrNum))


##  The largest number.
print("le plus grand nombre est ",max(newList))



##   The smallest number.
print("le plus petit nombre est ",min(newList))




##  exercice3

paragraph="As a result, it must first be converted to bytecode, converted to machine code before the program can be executed. Python is an interpreted language because, during execution, each line is interpreted to the machine language on the go. However, if we take the example of C++, the code needs to be compiled into an executable first, and then it can be executed. In Python, we can skip this compilation step (Python does it for us behind the scenes) and directly run the code."
print("ce paragraphe compte ",len(paragraph.split(" "))," mots")

print("ce paragraphe compte ",len(paragraph.split("."))," phase")

print("ce paragraphe compte ",len(set(paragraph.split(" ")))," mots unique")





##  exercice4



