#Name Jared Whittaker 
#Lab # 1
#Date 07/17/2024
#Lab Description Program to determine the occupancy max and population difference for meetings
#Variable Dictionary-------------------------------------------------------
meetname=""#This is the meeting name.
roommax=0#The Max occupancy for the room.
popattend=0#The expected attendance of the meeting.
popdif=0#The Difference between the population.
answer="y"#while loop for another meeting.
cont=""#asking the user if they would like the check another room.
#Imports-------------------------------------------------------------------
import sys
from os import system,name
#Functions-----------------------------------------------------------------
def difference(popattend,roommax):
    popdif=roommax-popattend
    return popdif
def clear():#clear for readability
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
def decision(response): #checking user response for errors
    while response.lower() != "y" and response.lower() != "n":
        print("That is an Invalid selection")
        response=input("Would you like to check another room? [Y/N]:")
        
        return response

#Main Code-----------------------------------------------------------------
while answer.lower()=="y":
    meetname=input("What is the name for your meeting?")
    roommax=float(input("What is the max occupancy of the room?"))
    popattend=float(input("What is the expected attendance of the meeting?"))
    popdif=difference(popattend,roommax)
    if popdif < 0:
        popdif=(popdif)
        print(f"You are currently over capacity by {abs(popdif):.0f}.")
        cont=input("Would you like to check another room? [Y/N]")
        answer=decision(cont)
        clear()
    if popdif == 0:
        popdif=(popdif)
        print(f"You are currently at capacity.")
        cont=input("Would you like to check another room? [Y/N]")
        answer=decision(cont)
        clear()
        
    if popdif > 0:
        popdif=abs(popdif)
        print(f"You are currently under capacity by {popdif:.0f} people.")
        cont=input("Would you like to check another room? [Y/N]")
        answer=decision(cont)
        clear()
print("THANK YOU FOR USING JAREDS MAGIC ROOM CHECKING ADDING MATH MACHINE CODE WOOOOOOO STAY IN SCHOOL!")