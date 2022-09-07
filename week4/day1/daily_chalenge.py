chaine = str(input("Entez une chaine de 10 caracteres"))
if len(chaine)<10:
	print("chaine pas assez long")
if len(chaine)>10:
	print("chaine trop long")

if len(chaine)==10:
	print(chaine[0], chaine[len(chaine)])

	y =""
	for x in chaine:
		y=y+x
		print(y)