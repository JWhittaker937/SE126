#Name Jared Whittaker
#Lab # 3B
#Date 07/31/2024
#Lab Description Voter Registation Lab SE116
#Variable Dictionary-------------------------------------
totalrecords=0
age=[]
voteid=[]
registered=[]
voted=[]
allowedtovote=0
registeredcount=0
votedcount=0
noteligible=0
notregistered=0
notvoted=0


#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
with open("Labs/Lab 3/lab3b.csv","r") as f:
    reader=csv.reader(f)
    for record in reader:
        totalrecords+=1
        voteid.append(record[0])
        age.append(int(record[1]))
        registered.append(record[2])
        voted.append(record[3])
for i in range(0,totalrecords):
    if (age[i])>= 18:
        allowedtovote+=1
    if (registered[i]).lower()=="y":
        registeredcount+=1
    if (voted[i]).lower()=="y":
        votedcount+=1
noteligible=totalrecords-allowedtovote
notregistered=allowedtovote-registeredcount
notvoted=allowedtovote-votedcount
print(f"Total Records|Eligible Voters|Ineligible|Registered Voters|Not Registered|Voted|Not Voted|")
print(f"{totalrecords:13}|{allowedtovote:15}|{noteligible:10}|{registeredcount:17}|{notregistered:14}|{votedcount:5}|{notvoted:9}|")
