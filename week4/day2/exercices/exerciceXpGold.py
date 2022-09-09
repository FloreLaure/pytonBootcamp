
##  exercice1

names = ['Samus', 'Cortana', 'V']
first=['Link', 'Mario', 'Cortana', 'Samus']

first_names=names + first
print(first_names)


##  exercice2

for x in range(1500,2501):
	if x%5==0:
		print(x)
	if x%7==0:
		print(x)



##  exercice3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input("Entrez votre nom\n")
for x in names:
	if x==name:
		print(names.index(x))
		break



##  exercice4

numb=input("Entrez 3 nombres")
print("The greatest number is:",max(numb.split(" ")))


##  exercice5

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
voyelle=["a","e","i","o","u","y"]
for x in alphabet:
	if x in voyelle:
		print(x,"est une voyelle")
	else:
		print(x,"est une consomne")
			

##  exercice6
mots=[]
lettre=input("Entrez une lette")
for i in range(1,8):
	mot=input("Entrer un mot")
	mots.append(mot)

for i in mots:
	if lettre in i:
		print(i.index(lettre))
	else:
		print(lettre," n'est pas dans ",i)