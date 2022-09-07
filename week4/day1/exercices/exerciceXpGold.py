##  exercice1

print((("Hello world\n")*4) + (("I love python\n")*4))



##  exercice2

a=int(input("Entrez un mois (1 à 12)\n"))
if 1 <= a <= 12:
	if 3 <= a <= 5:
		print("c'est le printemps")
	elif 6 <= a <= 8:
		print("c'est Eté")
	elif 9 <= a <= 11:
		print("c'est Automne")
	else:
		print("Hivers")
else:
	print("mauvais mois")



