from datetime import datetime
date = input("Entrez votre date de naissance sous le format DD/MM/YYYY : ")
date = date.split("/")
date = int(date[-1])
age = str(datetime.now().year - date)
age = int(age[-1])
gateau = "       _"

for x in range(int((9-age)/2)) :
    gateau += "_"
for x in range(10-(int((9-age)/2))) :
    if age != 0 :
        gateau += "i"
        age -= 1
    else :
        gateau += "_"
gateau += """
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
if (date % 4 == 0 and date % 100 != 0) or (date % 4 == 0 and date % 100 == 0 and date % 400 == 0) :
    print(gateau)
print(gateau)