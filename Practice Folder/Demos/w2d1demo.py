#Name Jared Whittaker
#Lab # Mini demo week 2 day 1
#Date 07/22/2024
#Lab Description Basic import of CSV and using info in csv files
#Variable Dictionary-------------------------------------
totalrecords = 0
sum_age=0
avgage=0
#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------

#Main Code-----------------------------------------------
with open("Practice Folder/W2D1baseinfo.csv") as csvfile:
    file = csv.reader(csvfile)
    for record in file:
        print(f"{record[0]:10}{record[2]:4}")
        sum_age+=int(record[2])
        totalrecords+=1
print("AINT NOTHING LEFT")
avgage=sum_age/totalrecords
print(f"Average age in file:{avgage:.2f}")