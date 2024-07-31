#Name Jared Whittaker
#Lab # w3d2 demo
#Date 
#Lab Description
#Variable Dictionary-------------------------------------
name=[]
age=[]
color=[]
animal=[]
totalage=[]
totalrecords=0
animalgrammer=[]
grammercorrection="a"
#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
with open("Practice Folder/Demos/classList_202140.txt") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
        totalrecords+=1
        name=(record[0])
        age=(record[1])
        color=(record[2])
        animal=(record[3])
        animalgrammer=(record[3][0])
        if animalgrammer.lower()=="a" or animalgrammer.lower()=="e" or animalgrammer.lower()=="i" or animalgrammer.lower()=="o" or animalgrammer.lower()=="u" or animalgrammer.lower()=="y":
            grammercorrection="an"
        else:
            grammercorrection="a"
        print(f"{name}'s favorite animal is {grammercorrection} {animal}.")