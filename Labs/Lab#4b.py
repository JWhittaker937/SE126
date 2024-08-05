#Name Jared Whittaker
#Lab # Lab 4 B
#Date 08/05/2024
#Lab Description Using lists to add house mottos for some nerdy tv show.
#Variable Dictionary-------------------------------------
totalrecords=0
firstname=[]
lastname=[]
age=[]
nickname=[]
allegiance=[]
motto=0
agetotal=0
housestark=0
housebaratheon=0
housetully=0
houselannister=0
housetargaryen=0
nightswatch=0
#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
with open("Labs/Lab4/lab4A_GOT_NEW.txt","r") as f:
    reader=csv.reader(f)
    for record in reader:
        totalrecords+=1
        firstname.append(record[0])
        lastname.append(record[1])
        age.append(record[2])
        nickname.append(record[3])
        allegiance.append(record[4])
for i in range(0,totalrecords):
    if allegiance[i]== "House Stark":
        motto="Winter is Coming"
        housestark+=1
    if allegiance[i]== "House Baratheon":
        motto="Ours is the fury."
        housebaratheon+=1
    if allegiance[i]=="House Tully":
        motto="Family. Duty. Honor"
        housetully+=1
    if allegiance[i]=="Night's Watch":
        motto="And now my watch begins."
        nightswatch+=1
    if allegiance[i]=="House Lannister":
        motto="Hear me roar!"
        houselannister+=1
    if allegiance[i]=="House Targaryen":
        motto="Fire & Blood."
        housetargaryen+=1
    agetotal+=int(age[i])
    averageage=agetotal/totalrecords
    print(f"Name: {firstname[i]:10}|Last name: {lastname[i]:15}|Age: {age[i]:3}|Nickname: {nickname[i]:20}|Allegiance: {allegiance[i]:20}|{motto:15}")
print(f"Total people: {totalrecords}|Average age: {averageage:3.0f}")
print(f"Allegiance to House Stark:        {housestark:3}|")
print(f"Allegiance to House Targaryen:    {housetargaryen:3}|")
print(f"Allegiance to House Baratheon:    {housebaratheon:3}|")
print(f"Allegiance to House Lannister:    {houselannister:3}|")
print(f"Allegiance to House Nights Watch: {nightswatch:3}|")
