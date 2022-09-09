##  exercice1

my_fav_numbers={3, 5, 7, 2, 3, 5}

my_fav_numbers.add(10)

my_fav_numbers.add(14)

my_fav_numbers.pop()

friend_fav_numbers={3,8,14,16,18,2}

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)







##  exercice2

##  No . Tuples are immutable lists, which means items can’t be changed.



## exercice3

basket = ["Banana","Apples","Oranges","Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket.clear()

print(basket)



## exercice4

floats=[ 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(floats)




## exercice5

for i in range(1,21,1):
	print(i)
for i in range(1,21,2):
	print(i)


##  exercice6

name = input("Entrez votre nom\n")   
while name != "Flore": 
	name=input("Entrez votre nom\n")   


##  exercice7
favorite_fruit = input("Entrez vos fuits preferé,separer les par un espace")
favorite_fruit.split(" ")
fruit = input("Entrez le nom d'un fruit")
for x in favorite_fruit:
	if x == fruit:
		print("vous avez choisis un de vos fruits preferé!!prendre plaisir")
	else:
		print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")




## exercice8






## exercice9





## exercice10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for sandwich in sandwich_orders:
	finished_sandwiches.append(sandwich)
	print("I made your ",sandwich)
	finished_sandwiches.remove(sandwich)






## exercice11