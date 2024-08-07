#Name Jared Whittaker  
#Lab # W4d2 demo
#Date 08/07/2024
#Lab Description Lists and hand population random and sequetional search
#Variable Dictionary-------------------------------------
dragonnames=["Drogon","Silverwing","Vermithor","Syrax","Meleys","Tim"]
dragonalias=["Good Boi","The Silver Lady","The Bronze Fury","The Goddess","The Red Queen","Death by powerpoint"]
totalrecords=len(dragonnames)
cont=0
#Imports-------------------------------------------------
import random
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------

dragonages = []
for i in range(0, len(dragonnames)):
    dragonages.append(random.randint(0, 500))
dragoninfo=[]
for i in range(0,len(dragonnames)):
    dragoninfo.append([dragonnames[i],dragonalias[i],dragonages[i]])
#for i in dragoninfo:
#    print(f"{i[0]} alias {i[1]} age {i[2]}")
for i in range(0,len(dragoninfo)):
    for x in range(0,len(dragoninfo[i])):
        print(f"{dragoninfo[i][x]}", end= " ")
    print()
        
#sequential search
searchdragon=input("Who are you looking for?")
found="n/a"
for i in range(0,len(dragonnames)):
    if searchdragon.lower()==dragonnames[i].lower():
        found=i
if found !="n/a":
    print(f"{searchdragon} was found in record #{found}\nName:{dragonnames[found]}| Alias:{dragonalias[found]}| Age:{dragonages[found]}")
else:
    print("wrong")