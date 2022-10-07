//chalenge 1

mot=input("Entrez un mot")
mot = {letter: [mot.index(i) for i in mot] for letter in mot}
print(mot)

// chalenge 2
wallet=8000


items_purchase = {
  "Apple": 4,
  "Honey": 3,
  "Fan": 14,
  "Bananas": 4,
  "Pan": 100,
  "Spoon": 2
}


payable=[article for article in items_purchase if items_purchase[article]<=wallet]
print(payable)
