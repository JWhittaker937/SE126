#Name Jared Whittaker
#Lab # 2
#Date 07 22 2024
#Lab Description Calculating the difference from a file and printing the non compliant 
#Variable Dictionary----------------------------------------
totalrecords=0 #record counter
popdiff=0 #difference variable for room max
compliantrecords=0 #this is the compliant records 
#Imports----------------------------------------------------
import csv
#Functions--------------------------------------------------
#Main Code--------------------------------------------------
with open("Labs/Lab2 data/lab2a.csv") as file:
    data=csv.reader(file)
    for record in data:
        popdiff=int(record[1])-int(record[2])
        totalrecords+=1
        if popdiff >=0:
            compliantrecords+=1
        if popdiff <0:
            popdiff=popdiff*-1
            print(f"{record[0]:20} IS OVER CAPACITY BY {popdiff:5} PEOPLE.")
            noncompliant=totalrecords-compliantrecords
    print(f"Total Records:      {totalrecords:5}\nCompliant Records:  {compliantrecords:5}\nOver Capacity rooms:{noncompliant:5}") #This outputs all the information 