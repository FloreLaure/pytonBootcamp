
##    exercice1

print(("Hello world\n")*4)



##   exercice2

print((99**3)*8)


##    exercice3

>>> 5 < 3 ## false

>>> 3 == 3 ## true

>>> 3 == "3" ## false

>>> "3" > 3 ## TypeError

>>> "Hello" == "hello"  ## false



##  exercice4

computer_brand = "HP"
print("I have a " + computer_brand + " computer")


##  exercice5

name="Flore"
age="21"
shoe_size="39"
info=("My name is " + name + " I have " + age +" year and my shoe size is " + shoe_size)
print(info)


##  exercice6

a=8
b=6
if (a>b):
	print("Hello world")



##  exercice7

a=int(input("Entrer un nombre\n"))
if (a%2 == 0):
	print("It is an even number")
else:
	print("It is an odd number")



##  exercice8

name=input("Entrer votre nom")
if name=="Flore":
	print("nous avons le meme nom")
elif name=="flore":
	print("nous avons le meme nom")
else:
	print("on a pas le meme nom")



## exercice9

pouce=int(input("Entrer votre taille en pouce\n"))
if taille > 145/2.54:
	print("vous pouvez rouler")
else:
	print("vous devez grandir encore")

