class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("miaou",3)  
cat2 = Cat("loulou",5) 
cat3 = Cat("mia",1) 
   
def ancien(): 
	maxi=max([cat1.age,cat2.age,cat3.age])
	print("le chat le plus agée est ", ,"il a ",maxi, " age") 

ancien()

