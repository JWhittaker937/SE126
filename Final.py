#Name Jared
#Lab # Final Exam
#Date 
#Lab Description
#Variable Dictionary-------------------------------------
accountname="" #just a simple account name used for personalization
realtor=0 #This determines the account type of the user.
menuselection=0 #Used for the section selection on the main menu
#yearbuilt= the year the property was built.
#bedcount= bedroom count of the property.
#bathcount= bathroom count of the property.
#squarefoot= squarefootage of the property.
#costperfoot= is the squarefootage divided by the cost.
#garagecount= would be the amount of cars you can fit in the garage.
#listprice=
#lastsold
#Imports-------------------------------------------------
import sys
import time
import csv
import os
from os import system,name
#Functions-----------------------------------------------
#Clear function
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
#Main menu screen
def mainmenu():
    print("menu here")

#class and functions for property
class property:
    def __init__(self,addressnumber,streetname,yearbuilt,bedcount,bathcount,squarefoot,listprice,costperfoot,garagecount,lastsold):
        self.addressnumber=addressnumber
        self.streetname=streetname
        self.yearbuilt=yearbuilt
        self.bedcount=bedcount
        self.bathcount=bathcount
        self.squarefoot=squarefoot
        self.listprice=listprice
        self.costperfoot=costperfoot
        self.garagecount=garagecount
        self.lastsold=lastsold
    def showyearbuilt(self):
        return self.yearbuilt
#Main Code-----------------------------------------------
