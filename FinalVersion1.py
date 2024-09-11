#Name Jared Whittaker
#Lab # Final V.1
#Date 9/10/2024
#Lab Description A property catolog and selector allowing people to search properties add them and import or export to a CSV file
#Variable Dictionary-------------------------------------
# In the class I created several variables starting with an ID number for the catalog.
# id number to list out the properties in a catalog.
# address, price, and a brief description of the property
#running as a while loop variable
#searching as the while loop variable in the catalog
#pages during the catalog and sorting process 
#pagesize determining the amount of properties shown per page of the catalog
#Imports-------------------------------------------------
import sys
import time
import os
from os import system,name
import csv
#Functions-----------------------------------------------
def clear(): #This is copied from cave explorer.
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
class property: #A class system with VERY basic identification of a house this class sytem is def something I want to explore more
    def __init__(self,idnumber,address,price,description,):
        self.idnumber=idnumber
        self.address=address
        self.price=price
        self.description=description
properties={ #I used an AI to extend the list outwards past 10 properties. I tried to get faker to work but I think my firewall doesn't like faker very much. Many of these are boring AI has no humor.
    "53": property("53", "867 Fake Street. Nowheresville USA", 404, "A scam set up by a fake prince."),"2": property("2", "530 Fake Street. Nowheresville USA", 300001, "Probably going to be bought by the Chinese."),"3": property("3", "9 Fake Street. Nowheresville USA", 65000, "No roof No walls the perfect DYI."),"4": property("4", "1 Notareel Street. Rehoboth USA", 99999999999, "Millennialss dream fridge box!."),"5": property("5", "2 Notareel Street. GonFishing USA", 24, "A different fake prince."),"6": property("6", "3 Notareel Street. JaysShirts USA", 250000000000, "A house previously known as Prince."),"7": property("7", "4 A Tree Street. TimIsOld USA", 659485, "Trapped in basement send help!!!"),"8": property("8", "5 Another Tree Street. Shud-Hav-Ben-NjenEar USA", 305000, "Walking distance from dump!"),"9": property("9", "6 Another Another Tree Street. WhyRuReadingThis USA", 205000, "Below trainstation! EASY access to helping the needy!"),"10": property("10", "7 Another Another Another Another Another Tree Street. Urmumshouse USA", 25, "Why are all the streets named after bloody trees!?!?!"),"11": property("11", "123 Main Street, Metropolis", 1500000, "A luxurious penthouse with stunning city views."),"12": property("12", "456 Elm Street, Riverside", 350000, "A cozy cottage with a backyard garden."),"13": property("13", "789 Oak Street, Downtown", 800000, "A modern loft with exposed brick walls."),"14": property("14", "101 Pine Street, Beachfront", 2000000, "A beachfront villa with a private pool."),"15": property("15", "123 Maple Street, Suburban", 450000, "A family-friendly home with a spacious backyard."),"16": property("16", "456 Cedar Street, Historic District", 600000, "A charming townhouse with original features."),"17": property("17", "789 Walnut Street, Mountain View", 550000, "A mountainside cabin with breathtaking views."),"18": property("18", "101 Willow Street, Countryside", 300000, "A farmhouse with plenty of land."),"19": property("19", "123 Birch Street, Urban", 700000, "A modern apartment with city amenities."),"20": property("20", "456 Chestnut Street, Waterfront", 1200000, "A waterfront townhouse with a marina view."),"21": property("21", "789 Poplar Street, Vineyard", 850000, "A vineyard estate with wine tasting room."),"22": property("22", "101 Olive Street, Desert", 400000, "A desert oasis with a pool and spa."),"23": property("23", "123 Elm Street, Forest", 350000, "A cozy cabin nestled in the woods."),"24": property("24", "456 Oak Street, Beachfront", 1800000, "A beachfront villa with ocean views."),"25": property("25", "789 Maple Street, Suburban", 475000, "A family-friendly home with a large backyard."),"26": property("26", "123 Birch Street, Urban", 700000, "A modern apartment with city amenities."),"27": property("27", "456 Chestnut Street, Waterfront", 1200000, "A waterfront townhouse with a marina view."),"28": property("28", "789 Poplar Street, Vineyard", 850000, "A vineyard estate with wine tasting room."),"29": property("29", "101 Olive Street, Desert", 400000, "A desert oasis with a pool and spa."),"30": property("30", "123 Elm Street, Forest", 350000, "A cozy cabin nestled in the woods."),"31": property("31", "456 Oak Street, Beachfront", 1800000, "A beachfront villa with ocean views."),"32": property("32", "789 Maple Street, Suburban", 475000, "A family-friendly home with a large backyard."),"33": property("33", "101 Pine Street, Mountain Retreat", 600000, "A secluded mountain cabin with stunning views."),"34": property("34", "123 Willow Street, Countryside", 325000, "A charming farmhouse with plenty of land."),"35": property("35", "456 Birch Street, Urban", 750000, "A modern loft with city amenities."),"36": property("36", "789 Chestnut Street, Waterfront", 1300000, "A waterfront townhouse with a marina view."),"37": property("37", "101 Poplar Street, Vineyard", 900000, "A vineyard estate with wine tasting room."),"38": property("38", "123 Olive Street, Desert", 425000, "A desert oasis with a pool and spa."),"39": property("39", "456 Elm Street, Forest", 375000, "A cozy cabin nestled in the woods."),"40": property("40", "789 Oak Street, Beachfront", 1900000, "A beachfront villa with ocean views."),"41": property("41", "101 Maple Street, Suburban", 490000, "A family-friendly home with a large backyard."),"42": property("42", "123 Pine Street, Mountain Retreat", 625000, "A secluded mountain cabin with stunning views."),"43": property("43", "456 Willow Street, Countryside", 350000, "A charming farmhouse with plenty of land."),"44": property("44", "789 Birch Street, Urban", 775000, "A modern loft with city amenities."),"45": property("45", "101 Chestnut Street, Waterfront", 1350000, "A waterfront townhouse with a marina view."),"46": property("46", "123 Poplar Street, Vineyard", 950000, "A vineyard estate with wine tasting room."),"47": property("47", "456 Olive Street, Desert", 450000, "A desert oasis with a pool and spa."),"48": property("48", "789 Elm Street, Forest", 390000, "A cozy cabin nestled in the woods."),"49": property("49", "101 Oak Street, Beachfront", 1950000, "A beachfront villa with ocean views."),"50": property("50", "123 Maple Street, Suburban", 510000, "A family-friendly home with a large backyard."),"51": property("51", "456 Pine Street, Mountain Retreat", 650000, "A secluded mountain cabin with stunning views."),"52": property("52", "789 Willow Street, Countryside", 375000, "A charming farmhouse with plenty of land."),"1": property("1", "no u. Nowheresville USA", 430, "A scam set up by a fake prince."),
}
nextid=1
def searchproperties(searchterm): #Using a simple search function. This is slow but allows ALL results not just the first one.
    results=[] # list for holding all results
    for propertyname,propertyobj in properties.items():
        if (searchterm.lower() in propertyobj.idnumber.lower() or searchterm.lower() in propertyobj.address.lower()): #Allowing to search for either address OR ID number 
            results.append(propertyobj) 
    return results
def addproperty():
    address=input("Enter property address: ")
    price=float(input("Enter property price: "))
    description=input("Enter property description: ")
    global nextid  #never had to declare something as global before it was a pain to understand. Def could have used that in cave explorer v.1
    idnumber=nextid
    nextid+=1#creating an id number this would be far more complex as the program gets developed but right now this ensures that
    #there are no duplicate id numbers
    newproperty=property(idnumber, address, price, description)
    properties[idnumber] = newproperty
    print("Property added successfully!")
def savepropertiestocsv(filename):# if this was used by multiple people this would be .appended and instead of accessing a CSV FILE I would guess this would link to a database.
    with open(filename, "w", newline="") as f:
        fieldnames=["IdNumber","address","price","description"]
        writer=csv.DictWriter(f, fieldnames=fieldnames) #Using a dictionary writer! This would be cool to try in cave explorer esp if I let other people work on the code
        writer.writeheader()
        for propertyid, propertyobj in properties.items():
            writer.writerow({
                 "IdNumber": propertyobj.idnumber,
                 "address": propertyobj.address,
                 "price": propertyobj.price,
                 "description": propertyobj.description })
            print("Properties saved to CSV successfully!")
def importfromcsv(): #Using the dictionary reader Again could be used in cave explore instead of me memorizing what row was what 
    #If this was to be used by multiple people then I should use the .append to ensure constant access to the file instead of holding the file open
    #during the programs opperation.
    csvfile=input("Enter the CSV file name: ")
    with open(csvfile,"r") as f:
        reader=csv.DictReader(f)
        for row in reader:
            idnumber=row["IdNumber"]
            address=row["address"]
            price=float(row["price"])
            description=row["description"]
            newproperty=property(idnumber,address,price,description)
            properties[idnumber]=newproperty
            print("Properties imported successfully!")
def listpropertiesbyid():# a sorting function and page display. This sorts and lists the properties by identification number and displays them in a cleanish format
    sortedproperties=sorted(properties.values(),key=lambda x: int(x.idnumber)) 
    pagesize=5 #defines the amount of properties shown per page. 5 fit well enough although for display on the projector I may change this number.
    pages=[sortedproperties[i:i+pagesize] for i in range(0, len(sortedproperties), pagesize)]
    currentpage=1 #pages dont start from 0 after all.
    searching=True#adding in a value so I dont have to use a break statement
    while currentpage <= len(pages) and searching==True:
        clear()
        print(f"Page {currentpage} of {len(pages)}")
        for propertyobj in pages[currentpage - 1]:
            print("-------------------------------------------------")
            print(f"ID Number: {propertyobj.idnumber}")
            print(f"Address: {propertyobj.address}")
            print(f"Price: ${propertyobj.price}")
            print(f"Description: {propertyobj.description}")
            print("-------------------------------------------------")
        print(f"Page {currentpage} of {len(pages)}")
        choice=input("Enter 'Next' to view the next page, or 'Prev' to view the previous page 'Quit' to return to the main menu: ").lower()
        if choice=="next" and currentpage < len(pages) or choice=="n" and currentpage < len(pages):
            currentpage+= 1
        elif choice=="prev" and currentpage > 1 or choice=="p" and currentpage > 1:
            currentpage-=1
        elif choice=="quit":
            clear()
            searching=False
        else:
            print("Invalid selection please try again.")
            time.sleep(1)#added in a sleep time so you can read the invalid selection but dont have to press enter
def mainmenu():
    running=True
    while running==True: 
        print("      Main Menu")
        print("==========================")
        print("1. Search for properties")
        print("2. Import from CSV")
        print("3. Save properties to CSV")
        print("4. Add property")
        print("5. Search Catalog")
        print("6. Quit")
        print("==========================")
        choice = input("Enter your choice (1-6): ")
        if choice=="1":
            searchterm=input("Enter search term: ")
            results=searchproperties(searchterm)
            if results:
                print("Search results:")
                for propertyobj in results:
                    clear()
                    print(f"Id Number: {propertyobj.idnumber}")
                    print(f"Address: {propertyobj.address}")
                    print(f"Price: ${propertyobj.price}")
                    print(f"Description: {propertyobj.description}")
                    print()
                    input("Press Enter to continue...")
            else:
                print("No properties found. Try searching through our catalog!")
        elif choice=="2":
            importfromcsv()
        elif choice=="3":
            filename=input("Enter the CSV file name: ")
            savepropertiestocsv(filename)
        elif choice=="4":
            addproperty()
        elif choice == "5":
            listpropertiesbyid()
        elif choice =="6":
            print("Goodbye!")
            running=False
        else:
            print("Invalid choice. Please try again.")
#Main Code-----------------------------------------------
mainmenu()