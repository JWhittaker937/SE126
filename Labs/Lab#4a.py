#Name Jared Whittaker
#Lab # Lab 4 A
#Date 08/05/2024
#Lab Description Avarage of a class using lists
#Variable Dictionary-------------------------------------
totalrecords=0
firstname=[]
lastname=[]
test1=[]
test2=[]
test3=[]
classavg=0
personalaverage=[]
testtotal=0
testtotal=0
numavg=[]
letteravg=[]
classtotal=0
#Imports-------------------------------------------------
import csv
import random
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
with open("Labs/Lab4/listPractice1.txt","r") as f:
    reader=csv.reader(f)
    for record in reader:
        totalrecords+=1
        firstname.append(record[0])
        lastname.append(record[1])
        test1.append(record[2])
        test2.append(record[3])
        test3.append(record[4])
for i in range(0,totalrecords):
    testtotal=int(test1[i])+int(test2[i])+int(test3[i])
    classtotal+=int(testtotal)
    personalaverage=int(testtotal)/3
    if personalaverage <60:
        letteravg="F"
    if personalaverage >= 60:
        letteravg="D"
    if personalaverage >= 70:
        letteravg="C"
    if personalaverage >= 80:
        letteravg="B"
    if personalaverage >= 90:
        letteravg="A"
    totaltests=int(totalrecords)*3
    classavg=classtotal/totaltests
    print(f"Name: {firstname[i]:10}|Last Name: {lastname[i]:13}|Test #1: {test1[i]:3}|Test #2: {test2[i]:3}|Test #3: {test3[i]:3}|Test Average: {personalaverage:4.0f}|Letter Grade: {letteravg:1}|")
    if classavg <60:
        classletteravg="F"
    if classavg >= 60:
        classletteravg="D"
    if classavg >= 70:
        classletteravg="C"
    if classavg >= 80:
        classletteravg="B"
    if classavg >= 90:
        classletteravg="A"
print(f"\nClass Average: {classavg}|\nClass Letter Average: {classletteravg}|")