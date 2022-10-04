

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


###   Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {
    'name': 'Zara',
    'creation_date': 1975, 
    'creator_name': ['Amancio', 'Ortega', 'Gaona'],
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton' ],
    'number_stores': 7000 ,
    'major_color':{
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']
        }
        
}



brand.update({"number_stores": 2})  ## Change the number of stores to 2.

print("les clients de Zara sont: ",brand['creator_name'])  ## Print a sentence that explains who Zaras clients are.


brand['country_creation']='Spain' ##  Add a key called country_creation with a value of Spain.


##    Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
key='international_competitors'
if (key in brand):
    brand["international_competitors"].append("Desigual")



##    Delete the information about the date of creation.
del(brand["creation_date"])


print((brand['international_competitors'])[-1])  ### Print the last international competitor.


print((brand['major_color'])['US'])  ###  Print the major clothes colors in the US. 



print(len(brand.items())) ### Print the amount of key value pairs (ie. length of the dictionary).
 

print(brand.keys())  ###  Print the keys of the dictionary.



####  Create another dictionary called more_on_zara

more_on_Zara={
    'creation_date': 1975,
    'number_stores': 10000
}



brand.update(more_on_Zara) ###  Use a method to add the information from the dictionary more_on_zara to the dictionary brand. 



print(brand["number_stores"]) ###  Print the value of the key number_stores






##  exercice4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for item in enumerate(users):
    print(zip(item))





