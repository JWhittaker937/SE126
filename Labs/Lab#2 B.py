#Name Jared Whittaker
#Lab # 2B
#Date 07/24/24
#Lab Description This lab is a basic reading of a file and 
#organization of data. 
#Variable Dictionary-------------------------------------\
totalrecords=0
desktopor=0#desktop or laptop
manname=0#Manufactur name
cpuname=0#proccessor name and generation
ramcount=0# Ram count on each pc
diskcount=0#how many hard drives
disksize1=0#size of disk 1 in GB
disksize2=0#size of disk 2 in GB
ossystem=0#What is the OS system
yearofsale=0#what year was the cpu sold?
#Imports-------------------------------------------------
import csv
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
with open("Labs/Lab2 data/lab2b.csv","r") as f:
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
            yearofsale=record[7]
            disksize2=("NONE")
        else:
            disksize1=(record[4])
            disksize2=(record[6])
            ossystem=(record[7])
            yearofsale=(record[8])
        print(f"{desktopor:7}|{manname:7}| CPU:{cpuname:2}| RAM:{ramcount:3}GB| Disk Count:{diskcount:2}| Disk1: {disksize1:5}| Disk2: {disksize2:5}|OS: {ossystem:3}| Year: 20{yearofsale:2}|")
    print(f"Total computers|{totalrecords}")