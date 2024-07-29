device=[]
brand=[]
cpu=[]
ram=[]
first_disk=[]
second_disk=[]
num_disks=[]
os=[]
yr=[]
records=0
import csv
with open("Labs/Lab 3/lab3a.csv") as csvfile:
    file=csv.reader(csvfile)
    for rec in file:
        records+=1
        device.append(rec[0])
for index in range(0,records):
    print(f"{device[index]}")