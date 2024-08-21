#W6D2 - Bubble Sorting & Binary Search Review

#https://www.google.com/search?q=bubble+sort+visualization&rlz=1C1GCHA_enUS1119US1119&oq=bubble+sort+visualization&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIICAQQABgWGB4yCAgFEAAYFhgeMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoFMg0ICBAAGIYDGIAEGIoF0gEIMzUwMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:7e94f359,vid:0BkoXZBbhfU,st:0 

#***IMPORTANT: 
#   In order to use binary search, 2 caveats must be fulfilled:
#      *the list we intend to search through is ORDERED
#      *the list we intend to search through is populated with UNIQUE VALUES (no repeats!)

#----IMPORTS-------------------------------------------------
import csv

#----FUNCTIONS-----------------------------------------------

#----MAIN CODE-----------------------------------------------
class_type = [] #rec[0] in file; repeats --> SEQUENTIAL
name = []       #rec[1] in file; unique  --> BINARY
meaning = []    #rec[2] in file; unique  --> BINARY
culture = []    #rec[3] in file; repeats --> SEQUENTIAL

with open("week6/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        print(rec)
        #rec is a 1D list and file is a 2D list
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])

#disconnect from file & test file connection + list storage
print(f"{'TYPE':8}   {'NAME':10}   {'CULTURE':10}   {'MEANING'}") #HEADER PRINT
print("-----------------------------------------------------------------------")
for i in range(0, len(class_type)):
    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
print("-----------------------------------------------------------------------\n")

#BINARY SEARCH: requires the list to be populated with unique values + be ORDERED

#BUBBLE SORT ALGORITHM
for i in range(0, len(name) - 1):#outter loop
    #print("OUTER LOOP! i = ", i)

    for index in range(0, len(name) - 1):#inner loop
        #print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):
            #print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

            #if above is true, swap places!
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp

            #swap all other values
            temp = class_type[index]
            class_type[index] = class_type[index + 1]
            class_type[index + 1] = temp

            temp = culture[index]
            culture[index] = culture[index + 1]
            culture[index + 1] = temp

            temp = meaning[index]
            meaning[index] = meaning[index + 1]
            meaning[index + 1] = temp
print("\t\tORDERED BY *NAME*")
print(f"{'TYPE':8}   {'NAME':10}   {'CULTURE':10}   {'MEANING'}") #HEADER PRINT
print("-----------------------------------------------------------------------")
for i in range(0, len(class_type)):
    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
print("-----------------------------------------------------------------------\n")

search = input("\nEnter the NAME you are looking for: ")

#now that it is ordered by name, we can now perform BINARY SEARCH
min = 0 
max = len(name) - 1
mid = int((min + max)/2)

while min < max and search != name[mid]:
    if search < name[mid]:
        max = mid - 1
    else:
        #search > name[mid]
        min = mid + 1
    mid = int((min + max)/2)

if search == name[mid]:
    print(f"We FOUND {search} !")
    print(f"{class_type[mid]:8}   {name[mid]:10}   {culture[mid]:10}   {meaning[mid]}")
else:
    print(f"We DID NOT FIND {search} :[")