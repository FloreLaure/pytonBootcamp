
mot = 'without,hello,bag,world'
mot = mot.split(',')
mot = sorted(mot)
mot1 = ""
for x in mot:
    mot1 += x + ','
print(mot1)