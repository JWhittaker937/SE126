#WEEK 9: FINAL REVIEW

#This review demo will cover all major topics from SE126.  It utilizes: 'finalReview_text.txt'
#Documentation has been added post demo to enhance understandig of the code

#in this review program, you will:
#   1 - connect to a file and import its data into lists
#               1a - the lists are UNEVEN so a filter system must be used
#               1b - count the total number of people in the file
#   2 - process the lists to print the original data to the console
#   3 - process the lists to find:
#               3a - the youngest person in the list
#               3b - the oldest person in the list
#               3c - the average age of the people in the list
#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#               4A - allow user to search multiple time
#               4a - sequential search will be performed w/ output to visualize search
#               4b - binary search will be performed w/ output to visualize search

#FUNCITONS-----------------------------------------------------------------------
def hello():

    print("Welcome to the SE126 FINAL REVIEW!")

def goodbye():

    print("Thank you for viewing the review. Now GO STUDY and kick some Finals butt!")


#a function that swaps values for bubble sorting
def swap(listname,position):
    temp=listname[position]
    listname[position]=listname[position+1]
    listname[position+1]=temp
    #this function could not return OR return TWO values ...

#a function that allows a user to search by sequential search or binary search
def search_menu():
    menu_options=[1,2,3]
    print("1. Sequential Search")
    print("2. Binary Search")
    print("3. Exit")
    try:
        response = int(input("Please enter your choice [1 - 3]: "))
    except:
        print("WRONG")
        return search_menu()

    #while response != 1 and response != 2 and response != 3:
    while response not in menu_options:
        print("*ERROR*ERROR*")
        response = int(input("Please enter your choice [1 - 3]: "))

    #this function should return the user's selection AFTER checking that it is a valid input()


#---------------------------------------------------------------------------------
import csv

hello()


num_rec = 0

#create empty lists in order to store file data
idCode = []
lastname = []
firstName = []
age = []
allegiance = []
num = [] #if == 1, no color2 value ... only when == 2 is there a color2 value
color1 = []
color2 = [] #only when num (rec[5] from file) is == 2 is there a color2 present

#1 - connect to a file and import its data into lists
with open("finalReview_text.csv") as csvfile:

    file = csv.reader(csvfile)

        #when reading files, each record is treated as a list
        #each field of data (rec[#]) represents a new value
    for rec in file:

            #this for loop will run for as many records (rows) of data in the file

            #store data into lists --> .append()
        idCode.append(rec[0])
        lastname.append(rec[1])
        firstName.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])
        num.append(rec[5])
        color1.append(rec[6])
        if rec[5]=="2":
            color2.append(rec[7])
        elif rec[5]=="1":
            color2.append("None")
        else:
            color2.append("Error")



            #1a - the lists are UNEVEN so a filter system must be used
            #(not all records in the file have a color2, so we must filter)




            #1b - count the total number of people in the file
            #add one to total number of records, necessary for for loop processing
        num_rec += 1 

print("Finished storing data from file. Disconnecting from file now.\n\n")


#   2 - process the lists to print the original data to the console
for i in range(0, num_rec):

    #the for loop will start with 'i = 0'
    #for loop will +1 to value of 'i' through each pass through the loop
    #for loop will run for 'num_rec' times (for each record in the list)
    #wherever 'i' is present, replace with current loop integer value

    print(f"{"idCode":10}"{"Last Name":15})




#   3 - process the lists to find:
#PROCESS = FOR LOOP! for loops were BUILT for list/array processing!

#Ask yourself: 
#If the AGE list were ordered in *increasing numeric* order, 
#where would you find:
#           - the youngest person in the list
#           - the oldest person in the list


#Ask yourself:
#What do you need to find an average? 
#               3c - the average age of the people in the list

#for i in range(0, num_rec):

    




#avg_age = #calculate average age









#   4 - a search option to search for id codes within the list
#           ** utilize menu '1. Sequential 2. Binary 3. Exit' that is printed from a function that returns the user's selection choice
#4A - allow user to search multiple time
#if the function has a RETURN we must store its return to use in our base program

#answer = "y" #allows us to get in loop

#while answer == "y":

    #call menu function so we have options from menu -- this function will be returning the user's selection and storing it into the var userChoice

#    if userChoice == 1:
        #4a - sequential search will be performed w/ output to visualize search

        #ask for search query


        #run sequential search




        #print results

#    if userChoice == 2:

        #4b - binary search will be performed w/ output to visualize search
        #BINARY SEARCH CAN ONLY BE USED ON ORDERED LISTS

        #ask for search query


        #sort list & linked data


        #binary search list



        #print results


#    if userChoice == 3: 

        #EXIT PROGRAM



    #which menu choices do NOT want to be asked if they want to run again?
#    if :

#        answer = 

#goodbye()