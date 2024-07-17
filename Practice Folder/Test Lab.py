#Name Jared Whittaker
#Lab #Week one practice
#Date 07/17/2024
#Lab Description
#Variable Dictionary-------------------------------------------------------
tempcount=0#This is how many units of data are being tracked
tempsum=0#This is the sum of all data added
answer="y"#This asks the user to continue
tempavg=0#This is the average of the tempatures 
temp=0#This is the temp added
tempc=0#the tempature in C
tempcavg=0#average of the temp in c
restart="y"
degree = u"\N{DEGREE SIGN}"
#Imports-------------------------------------------------------------------
#Functions-----------------------------------------------------------------
def converter(f):
    "This function is passed a temp F value, converts to C. and returns said value."
    c=(f-32)*(5/9)
    return c #literally returns to the point of function call
#Main Code-----------------------------------------------------------------
while answer.lower()=="y":
    temp= float(input(f"Enter a tempature #{tempcount+1} in Fahrenheit:"))
    tempcount = tempcount+1 #totaling the # temp values added
    tempsum= tempsum+temp #adding to the temp sum
    #convert f to c using a function which returns a value
    #tempc=(temp-32)*(5/9)
    tempc=converter(temp)
    print(f"Temperature:{temp:.1f}{degree}F | {tempc:.1f}{degree}C")

    #build a way out
    answer=input("Would you like to enter another tempature? [Y/N]:")
    while answer.lower() != "y" and answer.lower() != "n":
        print("Invalid entry")
        answer=input("Would you like to enter another tempature? [Y/N]:")
if tempcount != 0:
    tempavg = tempsum/tempcount
    tempcavg=converter(tempavg)
    print(f"You have entered {tempcount} temperatures for an average of {tempavg:.2f}{degree}F | {tempcavg:.1f}{degree}C.")
    print("Thanks for using the JARED AWESOME CODING AVERGAGE TEMPATURE EXTREME 4000!")
else:
    print("Okay Goodbye then nerd.")