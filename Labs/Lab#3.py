#Name Jared Whittaker
#Lab # 3A
#Date 07/29/2024
#Lab Description: Using the same list as the last lab find out the costs and amount of computers that are required to be replaced
#Variable Dictionary-------------------------------------
desktopor=0 #Is this a desktop or a laptop  
manname=0 #What is the manufacturor
cpuname=0 # What proccessor
ramcount=0 #ram count
diskcount=0 #how many disks
disksize1=0 #size of disk 1
disksize2=0 #size of disk 2
ossystem=0 #what os system is used
yearofsale=0 #when was the device purchased
desktopreplacecount=0 #how many desktops need to be replaced
laptopreplacecount=0 #how many laptops need to be replaced
totalrecords=0 #total records
totalcost=0 #total costs
desktopcost=0 #how much does it cost to replace all of the  desktops
laptopcost=0 #how much does it cost to replace all of the laptops 
laptopreplacecost=0 #how much does it cost to replace a single laptop
desktopreplacecost=0 #how much does it cost to replace a single desktop
replaceyear=0 #What is the year you wish to replace stuff if older
cont="y"
#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
while cont.lower()=="y":
    print("Welcome to the replacement software!")
    desktopreplacecost=input("What is the cost of replacement for a desktop? DO NOT ENTER COMMAS! $")
    laptopreplacecost=input("What is the cost of replacement for a laptop? DO NOT ENTER COMMAS! $")
    replaceyear=input("What is the cutoff year? Please enter the last two digets of the year only 20")
    laptopreplacecost=int(laptopreplacecost)
    desktopreplacecost=int(desktopreplacecost)
    replaceyear=int(replaceyear)
    with open("Labs/Lab 3/lab3a.csv","r") as f:
        reader=csv.reader(f)
        for record in reader:
            totalrecords+=1
            desktopor=str(record[0])
            if desktopor.lower()==("d"):
                desktopor="Desktop"
            if desktopor.lower()==("l"):
                desktopor="Laptop"
            manname=str(record[1])
            if manname.lower()==("dl"):
                manname=("Dell")
            if manname.lower()==("hp"):
                manname=("HP")
            if manname.lower()==("gw"):
                manname=("GateWay")
            cpuname=str(record[2])
            ramcount=record[3]
            diskcount=int(record[5])
            if diskcount ==1:
                disksize1=record[4]
                ossystem=record[6]
                yearofsale=int(record[7])
                disksize2=("NONE")
                if yearofsale <= 16 and desktopor=="Desktop":
                    desktopreplacecount+=1
                if yearofsale <= 16 and desktopor=="Laptop":
                    laptopreplacecount+=1
            else:
                disksize1=(record[4])
                disksize2=(record[6])
                ossystem=(record[7])
                yearofsale=int(record[8])
                if int(yearofsale) <= int(replaceyear) and desktopor=="Desktop":
                    desktopreplacecount+=1
                if int(yearofsale) <= int(replaceyear) and desktopor=="Laptop":
                    laptopreplacecount+=1
    laptopcost=laptopreplacecount*laptopreplacecost
    desktopcost=desktopreplacecount*desktopreplacecost
    totalcost=desktopcost+laptopcost
    print(f"{totalrecords:5} Total computers scanned.")
    print(f"{desktopreplacecount:5} Desktops need to be replaced this will cost ${desktopcost:8}.")
    print(f"{laptopreplacecount:5} Laptops need to be replaced this will cost  ${laptopcost:8}.")
    cont=input(     "Would you like to run this program again? Y/N")