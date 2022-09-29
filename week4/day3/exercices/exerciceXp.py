

## exercice1

##  Convert the two following lists, into dictionaries.
##  Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionnaire=dict(zip(keys, values))
print(dictionnaire)



##  exercice2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
tolal=0
for x, y in family.items():
    if 0<=y<3:
        print("c'est gratuit pour ",x)
    elif 3<=y<=10:
        print("le billet est de 10$ pour ",x)
        total=tolal+10
    else:
        print("le billet est de 15$ pour ",x)
        total=tolal+15

print("le total est ",tolal)


##  xercice3

brand = {
    "name": "Zara" 
    "creation_date": 1975 
    "creator_name": ["Amancio", "Ortega", "Gaona" ]
    "type_of_clothes": ["men", "women", "children", "home"] 
    "international_competitors": ["Gap", "H&M", "Benetton" ]
    "number_stores": 7000 
    "major_color":{
        "France": "blue" 
        "Spain": "red" 
        "US": ["pink", "green"]
        }
        
}
brand.update({"number_stores": 2})
brand.append("country_creation":Spain)

print(brand)











##  exercice4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for item in enumerate(users):
    print(list(item))





