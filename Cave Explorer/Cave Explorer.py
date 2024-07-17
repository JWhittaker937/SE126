import random
import sys
import time
import csv
from os import system,name
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")
#Variables
charn=""
clsn=""
cls=0
clshp=1
hpmax=1
hp=1
clsm=0
manamax=0
mana=0
wepl=0
weph=0
wepn=0    
blkl=0
blkm=0
search=0
sense=0
cont="1"
gameon="1"
coins=0 #coins value for the player
npchp=0 #NPChp value to be set based on the room roll
xp=0 #starting xp
xpmax=100 #starting xp to require to level changes as people level
lvl=1 #starting level
roomlvl=10 #room level value
costitem1=30 #cost of item 1
costitem2=40 #cost of item 2
costitem3=50 #cost of item 3
#Defs BELOW
#SAVE FILE HERE COPIED FROM GOOGLE BARD
def create_save_file():
    with open("save_data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["charn", "cls", "xp", "xpmax", "hp", "hpmax", "mana", "manamax", "roomlvl", "coins", "costitem1", "costitem2", "costitem3", "weph", "clsn"])
        writer.writerow([charn, cls, xp, xpmax, hp, hpmax, mana, manamax, roomlvl, coins, costitem1, costitem2, costitem3, weph, clsn])
#I AM TRYING TO LEARN THIS SECTION    
def nomana():
    print("You do not have enough mana to cast this spell")
def gameover():#originally I typed this out everytime man that saved like 200 lines
    print("----------------------------------")
    print(" GGGGGG  AAAAAAA  M     M EEEEEEE ")
    print("GG    G AAA   AAA M     M E       ")
    print("G       A       A MM   MM E       ")
    print("G   GGG A       A M MMM M EEEEEEE ")
    print("G     G AAAAAAAAA M  M  M E       ")
    print("G     G A       A M     M E       ")
    print("GG    G A       A M     M E       ")
    print(" GGGGGG A       A M     M EEEEEEE ")
    print("----------------------------------")
    print(" 00000  V       V EEEEEEE RRRRRR  ")
    print("00   00 V       V E       R     R ")
    print("0     0 V       V E       R    R  ")
    print("0     0 V       V E       RRRRRR  ")
    print("0     0 V       V EEEEEEE R  R    ")
    print("0     0  V     V  E       R   R   ")
    print("00   00   V   V   E       R    R  ")
    print(" 00000     VVV    EEEEEEE R     R ")
    print("----------------------------------")
def stats():#simple stats chart that will be displayed when called
    print("--------------------------------------")
    print("You are",charn,"a level",lvl,clsn)
    print("HP:  ",hp,"/",hpmax,"  Weapon: ",wepn,)
    print("MANA: ",mana,"/",manamax," Damage:{:2.0f} -{:2.0f}".format(wepl,weph))
    print("XP:   ",xp,"/",xpmax,"  Coins:",coins)
    print("---------------------------------------")
#monster loot table to be rolled after every monster kill
lootl=0
looth=10
loot_table = {
    0:0,
    1:2,
    2:4,
    3:6,
    4:8,
    5:10,
    6:12,
    7:16,
    8:20,
    9:30,
    10:50,
    }
def loot():
    lootroll=random.randint(lootl,looth)
    return loot_table[lootroll]
#chest loot table used during the chest room
chestll=0
chestlh=5
chestloottable = {
    0:0,
    1:10,
    2:20,
    3:30,
    4:50,
    5:100,
    }
def chestloot():
    chestlootroll=random.randint(chestll,chestlh)
    return chestloottable[chestlootroll]
#BAD GUYS
#goblin values 
gobhp=10 #current goblin HP to be edited when I figure how to make a difficulty setting
gobhpmax=10 #gob max hp
gobwepl=0 #lowest goblin can hit
gobweph=2 #highest goblin can hit
gobxp=10 #xp awarded when goblin is slain
#Orc
orchp=20
orchpmax=20
orcwepl=0
orcweph=5
orcxp=25
#Siren
sirhp=35
sirhpmax=35
sirwepl=1
sirweph=5
sirxp=50
#Dragon
draghp=100
draghpmax=100
dragwepl=0
dragweph=15
dragxp=250
#SkeletonWarrior
skelhp=15
skelhpmax=15
skelwepl=0
skelweph=5
skelxp=15
#Lich
lichhp=75
lichhpmax=75
lichwepl=2
lichweph=8
lichxp=300
#TRAP detection
trapl=0 #lowest value the trap can roll for how well it is hidden
traph=5 #highest value the trap can roll for its hidden stat
trapdmgl=0 #lowest amount of damage the trap can do
trapdmgh=3 #highest amount of damage the trap can do
trpxp=10 #xp for finding the trap
def trapdmgroll(): #rolling trap damage def
    trapdmg=random.randint(trapdmgl,trapdmgh)
    return trapdmg
def traproll(): #rolling the hidden stat of the trap
    trapdif=random.randint(trapl,traph)
    return trapdif
def searchroll(): #rolling the characters searching is added to the search skill later on
    searchdc=random.randint(0,3)
    return searchdc
#Random room gen outline of the rooms and simple dialog for each room
def empty():
    print("This room appears to be empty.")
def goblin():
    print("You enter the room and spot a goblin!")
def chest():
    print("You see a chest in the middle of the room.")
def orc():
    print("A strong orc warrior stands before you ready for a fight!")
def dragon():
    print("A massive red dragon glares at you! This is going to hurt...")
def sirein():
    print("A young woman of incredible beauty sits on the floor in this room.")
def trapr():
    print("This room appears to be empty.")
def skeletonw():
    print("A skeletal warrior charges you he moves quick for someone with no muscle!")
def lich():
    print("Cold fills the room as you spot the masked figure floating in the center of the room")
    print("The glowing eyes of the lich burn with fury as it lifts a wand ready to fight")
#room generation remember the room level sets the max it can roll and the room level changes as the char levels
roomtable = {
    0:"empty",
    1:"empty",
    2:"chest",
    3:"goblin",
    4:"goblin",
    5:"goblin",
    6:"goblin",
    7:"orc",
    8:"orc",
    9:"skeletonw",
    10:"trap",
    11:"goblin",
    12:"trap",
    13:"orc",
    14:"sirein",
    15:"dragon",
    16:"skeletonw",
    17:"skeletonw",
    18:"skeletonw",
    19:"lich",
    20:"chest",
    21:"skeletonw",
    22:"skeletonw",
    23:"skeletonw",
    24:"skeletonw",
    25:"lich",
    }
def roomroll(): #room roll based on the roomlvl
    return roomtable[random.randint(0,roomlvl)]
#Room description table "funny" dialog that appears in every room to add some humor
roommodtable= {
    0:"is unnaturally cold. Your breath is clearly visible.",
    1:"is eire and sinister. Mist clings to the floor.",
    2:"is very warm. It would be relaxing if not for the bones.",
    3:"is pitch black. You can barely see your feet.",
    4:"is cool and you feel a slight breeze.",
    5:"seems to sway. Honestly you feel slightly sick.",
    6:"smells of garlic. At Least no vampires in this version.",
    7:"seems to be made of cheese? Probably not best to eat.",
    8:"resembles a doll house. Now this is just creepy.",
    9:"coughs politely.",
    10:"is judging you.",
    11:"would never give you up.",
    12:"would never let you down.",
    13:"would never go around and hurt you.",
    14:"has a small bird trying to fly while holding a coconut struggling in the corner.",
    15:"seems to be home to a family of rats. They are quite an unusual size",
    16:"is dark. In the corner you spot two large glowing eyes glaring right at you",
    17:"seems to be in another world.\nA sign above you says Central Park Zoo",
    18:"is bare except for a lone flower pot in the corner.\nWhen you enter you could have sworn you heard the flower complaining.\nOh no not again",
    19:"is for copyright reasons strangely silent.",
    20:"brings all the boys to the yard.",
    21:"let the dogs out.",
    22:"comes into view.\nWooden floor and swaying from side to side.",
    23:"shouts IT'S MY MONEY AND I NEED IT NOW!",
    24:"in a quiet voice asks you politely to take your shoes off.",
    25:"is filled with the sounds of smoooooth jazz.",
    26:"You can smell the sea from where you stand.\nWater splashing in from the round windows tells you that you aren't in the cave anymore.",
    27:"appears to have landed on someone.\nYou spot some red slippers on the feet sticking out.",
    28:"seems to be a tunnel. You spot two bright lets off to the right.\nThey are getting closer.\nThe room starts to shake!.",
    29:"is OUCH! the room has a really short door frame!",
    30:"has padded walls. Maybe its where you belong.",
    31:"another adventurer you wave exictedly! Oh its just a mirror...",
    32:"is coded in Python!",
    33:"",
    34:"",
    35:"",
    36:"",
    37:"",
    38:"",
    39:"",
    40:"",
    41:"",
    42:"",
    43:"",
    44:"",
    45:"",
    46:"",
    47:"",
    48:"",
    49:"",
    50:"",
    51:"",
    52:"",
    53:"",
    55:"",
    56:"",
    57:"",
    58:"",
    59:"",
    60:"",
    }
def roommod(): #calling a random room modification
    return roommodtable[random.randint(0,31)]
#Character sheet and start of game.
#char sheet
print("--------------------")
print("--------CAVE--------")
print("------EXPLORER------")
print("--------------------")
print("-----1.New-game-----")
print("--------------------")
print("-----2.Loadsave-----")
print("--------------------")
print("--BY----------------")
print("--JARED--WHITTAKER--")
print("--------------------")
loadgame=input()
clear()
if loadgame=="2":
    with open("save_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            charn = row[0]
            cls = row[1]
            xp = row[2]
            xpmax = row[3]
            hp = row[4]
            hpmax = row[5]
            mana = row[6]
            manamax = row[7]
            roomlvl = row[8]
            coins = row[9]
            costitem1 = row[10]
            costitem2 = row[11]
            costitem3 = row[12]
            weph = row[13]
            clsn = row[14]
        xp=int(xp)
        xp = int(xp)
        xpmax = int(xpmax)
        hp = int(hp)
        hpmax = int(hpmax)
        mana = int(mana)
        manamax = int(manamax)
        roomlvl = int(roomlvl)
        coins = int(coins)
        costitem1 = int(costitem1)
        costitem2 = int(costitem2)
        costitem3 = int(costitem3)
        weph = int(weph)
elif loadgame=="1":
    charn=input("What is your character's name? ")
    print("Select your class!")
    cls=input("1. Fighter\n2. Wizard\n3. Barbarian\n")
    if cls == "2":
        clsn="Wizard"
        #stats
        clshp=10 # class hp min
        hpmax=clshp #class hp max for level 1
        hp=hpmax #hp being set to hp max this value is only here to be edited when I figure out item and equipment slots
        clsm=20 #class mana and spell points 
        manamax=clsm #setting the class mana to max mana again incase I need to edit it with equipment
        mana=manamax #setting mana = to maxmana
        #weapon
        wepl=2 #lowest roll the attack can hit
        weph=4 #highest roll the attack can hit
        wepn="Wand" #weapon name for dialog
        #block
        blkl=0 #block value low
        blkm=1 #block value max
        search=3 #base search skill
        sense="arcane senses" #name of search skill for dialog
    if cls == "1":
        clsn="Fighter"
        #stats
        clshp=20
        hpmax=clshp
        hp=hpmax
        clsm=10
        manamax=clsm
        mana=manamax
        #weapon
        wepl=1
        weph=7
        wepn="Sword"
        #block
        blkl=0
        blkm=5
        search=2
        sense="intuition"
    if cls == "3":
        clsn="Barbarian"
        #stats
        clshp=15
        hpmax=clshp
        hp=hpmax
        clsm=0
        manamax=clsm
        mana=manamax
        #weapon
        wepl=0
        weph=10
        wepn="Axe"    
        #block
        blkl=0
        blkm=3
        search=1
        sense="dumbluck"
if loadgame=="2":
    clear()
    cont="2"
elif loadgame=="1":
    print("You begin your adventure just inside the cave...")
    print() #Below is starting dialog based on your class selection
    if cls =="1":
        print("You are a hardened Fighter from many campaigns.\nYou have been sent here to help the nearby town deal with the evil inside.\nHopefully after this job you can retire.")
        pause=input("Press Enter to continue...")
        clear()
    elif cls =="2":
        print("Fresh from Wizarding school you've taken up a job.\nTo clear the nearby cave. This will help to pay off your student debt.")
        pause=input("Press Enter to continue...")
        clear()
    elif cls =="3":
        print("YOU STRONG! YOU BREAK CAVE! HIT GOBLINS HARD!")
        pause=input("PRESS ENTER TO CONTINUE!")
        clear()
#GAME ON The main game loop only ended when dying or game exit.
while gameon=="1":
#TOWN the town section for buying items healing etc
    while cont=="2":
        clear()
        if hp <=0:
            print("You have died!")
            gameover()
            cont=-10
            pause=input()
            break
        stats()
        print("You stand in the middle of town what would you like to do?")
        towncon=input("1.Tavern         2.Shop \n3.Enter the Cave 4.Exit Game ")
        clear()
        #TAVERN
        if towncon=="1":
            stats()
            print("You enter a dimly lit tavern with a lone bartender.")
            act1=input("1. Buy a drink of restoration 10 coins\n2. Leave ")
            if act1=="1":
                if coins >= 10:
                  print("The drink heals you and restores your mana!")
                  hp=hpmax
                  mana=manamax
                  coins=coins-10
                  pause=input("Press Enter to continue...")
                  clear()
                else:
                    clear()
                    print("You dont have enough coins!")
                    pause=input("Press Enter to continue...")
            if act1=="2":
                towncon=-10
        if towncon=="2":
            stats()
            print("Welcome to my store!")
            print("What are you looking to buy today?")
            print("1. Ring of Striking +1 ATTACK ",costitem1,"coins\n2. Cloak of Mana +10 Mana ",costitem2,"coins\n3. Crown of Health +10HP ",costitem3,"coins\n4. Leave")
            itembuy=input()
            if itembuy=="1":
                if coins >=costitem1:
                    print("You purchased the Ring of Striking\nThis item adds +1 to your MAX Damage when you attack!")
                    weph=weph+1
                    coins=coins-costitem1
                    costitem1=costitem1+5
                else:
                    print("You dont have enough money.")
            if itembuy=="2":
                if coins >= costitem2:
                    print("You purchased the Cloak of Mana!\nThis item adds +10 to your MAX mana!")
                    coins=coins-costitem2
                    manamax=manamax+10
                    costitem2=costitem2+5
                else:
                    print("You dont have enough money.")
            if itembuy=="3":
                if coins >= costitem3:
                    print("You purchased the Crown of Health!\nThis item adds +10 to your Max HP!")
                    hpmax=hpmax+10
                    coins=coins-costitem3
                    costitem3=costitem3+5
                else:
                    print("You don't have enough money.")
            if itembuy=="4":
                print("You leave the store.")
            pause=input("Press Enter to continue...")
            clear()
        if towncon=="3":
            cont="1"
        if towncon=="4":
            cont=-10
            gameover()
            print("Saving game")
            create_save_file()
            pause=input("Press Enter to continue")
            clear()
            gameon="2"
    while cont=="1":
        clear()
        while xp >= xpmax:
            lvl=lvl+1
            print("LEVEL UP!",charn," is now a ",lvl,clsn,"!")
            xp=xp-xpmax
            hpmax=hpmax+5
            manamax=manamax+5
            if lvl % 2 ==0:
                weph=weph+1
            hp=hpmax
            mana=manamax
            roomlvl=roomlvl+2
            if roomlvl>25:
                roomlvl=25
            print("The dungeon is getting harder...")
            pause=input("Press Enter to continue...")
            xpmax=xpmax+50
            clear()
        if hp <=0:
            print("You have died!")
            gameover()
            pause=input()
            cont=-10
        roomroll()
#START OF EMPTY ROOM--------------------------------------
        if roomroll()=="empty":
            roomcon=0
            clear()
            empty()
            print("The room ",roommod())
            print()
            while roomcon==0:
                act1=input("What do you do?\n1. Search the room 2. Stats \n3. Venture Deeper  4. Leave Dungeon ")
                clear()
                if act1=="1":
                    print("You search the room but find nothing.")
                if act1=="2":
                    stats()
                if act1=="3":
                    print("You venture deeper into the cave!")
                    time.sleep(2)
                    cont="1"
                    roomcon=1
                if act1=="4":
                    print("You make your way out of the cave back to town")
                    cont="2"
                    if cont=="2":
                        break
                    roomcon=1
#END OF EMPTY ROOM------------------------
#START OF GOB FIGHT ROOM-----------
        if roomroll() == "goblin":
            clear()
            goblin()# starting dialog showing whats in the room
            print("The room ",roommod())
            npchp=gobhp# setting the npchp to the rolled NPC this allows me to copy and paste the room
            npchpmax=gobhpmax #and only have to edit these values up here to save on me typing
            npcwepn="crude axe" #npc weapon name
            npcn="Goblin Scout" #npc name to be displayed at the top
            npcweph=gobweph
            npcwepl=gobwepl
            npcxp=gobxp
            stund=0 #is the hostile stunned?
            npcalive=1 #npc alive loop value
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0: #struggled to get this death to function
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")#basic hud to be displayed on EVERY page
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")#shows the npc and your character stats
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)#rolling damage values
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:#checking if NPC is stunned
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:#NPC can be stunned for multiple turns so this is needed
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()#currently blocking which is this selection HAS NO benifit will be adding a 
                        print(charn,"Attempts to block!")#parry damage in future maybe like 1d4 although idle doesnt
                        if stund==0:#support the 1d4 and ill have to make another list.
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":#spells each spell depends on class and barbarian uses HP instead of MANA
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:# cost of spell
                                    spln="fireball"
                                    spldmgl=1 #converting spell into basic values so I can copy paste if I 
                                    spldmgh=10 #wanted to add more then 1 spell per char
                                    spldmg=random.randint(spldmgl,spldmgh) #rolling spell damage
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg#NPC HP - spell
                                    mana=mana-3#subtracting mana
                                    if stund==0: #letting the NPC hit back if they are not stunned
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()#NOT NUFF MANA NERD
                            elif cast=="2":
                                clear()
                                if mana >= 5:#healing spell cost
                                    heall=2#healing spell min
                                    healh=8#healing spell max
                                    heala=random.randint(heall,healh)#rolling heal value
                                    if hp + heala > hpmax:#checking for OVER heal
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:#checking if NPC is stunned
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)#stun roll for the shield bash skill
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax#this spell heals if the spell does enough damage
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()#displays stats then lets player read before moving on
                        pause=input("Press Enter to continue")
                        clear()
                
                print("---------------------------------------")
                npcloot=(loot())#rolling NPC LOOT
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")#asking if player wants to continue.
                if cont== "2":#CURRENT BUG player sometimes wont exit the dungeon when trying to 
                    break#but will be able to exit with no issues AFTER they finish another room
                npcalive=0
            
#END OF GOB FIGHT ROOM---------
#START OF TRAP ROOM---------------
        if roomroll()=="trap":
            clear()
            trapcon="n"#setting the trap loop this lets players search multiple times before they leave
            trap=1#turning on the trap
            trapr()#dialog of the trap
            if hp <=0:
                    print("You have died!")
                    gameover()
                    pause=input()
                    cont=-10
                    break
            print("The room ",roommod())
            print()#this room is the SAME as the empty room so that the player cant tell they are in a trap
            while trapcon=="n":
                act1=input("What do you do?\n1. Search the room 2. Stats\n3. Venture Deeper  4. Leave Dungeon ")
                if act1=="1":
                    trapdc=(traproll())#rolling the trap hidden stat
                    searchcheck=(searchroll()+search)#rolling the character search skill
                    if trap==1:#if trap is still on
                        if trapdc > searchcheck:#did they find it?
                            clear()
                            print("You search the room but find nothing.")
                        elif trapdc <= searchcheck:#yes they did 
                            clear()
                            print("With a bit of",sense," you spot the trap and disable it!")
                            print("You gain ",trpxp,"XP!")
                            time.sleep(2)#awarding xp and sleeping so player can read
                            xp=xp+trpxp
                            trap=0#turning off trap
                    else:
                        clear()#if player tries to search again when the trap is disabled
                        print("You have already found and disabled the trap.")
                if act1=="2":
                    clear()
                    stats()#displays stats as before
                if act1=="3":
                    if trap==1:#you tried to leave and the trap wasnt off
                        print("You have sprung a trap!")
                        trapincdmg=trapdmgroll()
                        print("You take",trapincdmg,"Dmg!")#rolling and taking trap damage
                        time.sleep(2)
                        hp=hp-trapincdmg
                        if hp <=0:#DID YOU DIE TO A TRAP THAT CAN ONLY MAX ROLL A 3?!?!?! REALLY?!
                            print("You have died!")
                            gameover()
                            pause=input()
                            cont=-10
                        else:#disables the trap after you take damage
                            trapcon="y"
                    if trap==0:#if you disabled it just lets you leave
                        trapcon="y"
                if act1=="4":#trying to leave for the town
                    print("You make your way out of the cave back to town")
                    if trap==1:#DID YOU DISABLE THE TRAP BEFORE TRYING TO LEAVE?!!?!
                        print("You have sprung a trap!")
                        trapincdmg=trapdmgroll()
                        print("You take",trapincdmg,"Dmg!")
                        time.sleep(2)
                        hp=hp-trapincdmg
                        if hp <=0:#Guess not
                            print("You have died!")
                            gameover()
                            pause=input()
                            cont=-10
                        else:#well its off now
                            trapcon="y"
                            cont="2"
                    else:#YAY you looked before you lept
                        cont="2"
                        trapcon="y"
#END OF TRAP ROOM
#START OF ORC FIGHT ROOM
        if roomroll() == "orc":
            clear()
            orc()
            print("The room ",roommod())
            npchp=orchp
            npchpmax=orchpmax
            npcwepn="great axe"
            npcn="Orc Warrior"
            npcweph=orcweph
            npcwepl=orcwepl
            npcxp=orcxp
            stund=0
            npcalive=1
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0:
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()
                        print(charn,"Attempts to block!")
                        if stund==0:
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:
                                    spln="fireball"
                                    spldmgl=1
                                    spldmgh=10
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-3
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                            elif cast=="2":
                                clear()
                                if mana >= 5:
                                    heall=2
                                    healh=8
                                    heala=random.randint(heall,healh)
                                    if hp + heala > hpmax:
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()
                        pause=input("Press Enter to continue")
                        clear()
                print("---------------------------------------")
                npcloot=(loot())
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")
                if cont== "2":
                    break
                npcalive=0
#END OF orc FIGHT ROOM
#START OF sirein FIGHT ROOM
        if roomroll() == "sirein":
            clear()
            sirein()
            print("The room ",roommod())
            npchp=sirhp
            npchpmax=sirhpmax
            npcwepn="her claws"
            npcn="Sirein"
            npcweph=sirweph
            npcwepl=sirwepl
            npcxp=sirxp
            stund=0
            npcalive=1
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0:
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()
                        print(charn,"Attempts to block!")
                        if stund==0:
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:
                                    spln="fireball"
                                    spldmgl=1
                                    spldmgh=10
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-3
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                            elif cast=="2":
                                clear()
                                if mana >= 5:
                                    heall=2
                                    healh=8
                                    heala=random.randint(heall,healh)
                                    if hp + heala > hpmax:
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()
                        pause=input("Press Enter to continue")
                        clear()
                print("---------------------------------------")
                npcloot=(loot())
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")
                npcalive=0
#END OF sirein FIGHT ROOM
#START OF Chest room
        if roomroll()=="chest":
            roomcon=0
            clear()
            chest()
            print("The room ",roommod())
            chestvalue=(chestloot())#rolling the value in the chest
            print()
            chestopened=0
            while roomcon==0:
                act1=input("What do you do?\n1. Search the chest! 2. Stats \n3. Venture Deeper    4. Leave Dungeon")
                if act1=="1":
                    if chestopened==0:
                        clear()#if the chest wasnt already openned letting you open and loot it
                        print("You search the chest and find",chestvalue,"coins!")
                        coins=coins+chestvalue
                        chestopened=1#setting the chest to opened
                    else:
                        clear()
                        print("You have already looted this chest")#if you try to search an opened chest
                if act1=="2":
                    clear()
                    stats()#displays stats as before
                if act1=="3":
                    print("You venture deeper into the cave!")
                    roomcon=1#lets you leave the room
                    cont="1"
                if act1=="4":
                    print("You make your way out of the cave back to town")
                    roomcon=1#lets you leave the room
                    cont="2"
#skeleton roll
        if roomroll() == "skeletonw":   
            clear()
            skeletonw()
            print("The room ",roommod())
            npchp=skelhp
            npchpmax=skelhpmax
            npcwepn="rusted sword"
            npcn="Skeleton Warrior"
            npcweph=skelweph
            npcwepl=skelwepl
            npcxp=skelxp
            stund=0
            npcalive=1
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0:
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()
                        print(charn,"Attempts to block!")
                        if stund==0:
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:
                                    spln="fireball"
                                    spldmgl=1
                                    spldmgh=10
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-3
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                            elif cast=="2":
                                clear()
                                if mana >= 5:
                                    heall=2
                                    healh=8
                                    heala=random.randint(heall,healh)
                                    if hp + heala > hpmax:
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()
                        pause=input("Press Enter to continue")
                        clear()
                print("---------------------------------------")
                npcloot=(loot())
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")
                if cont== "2":
                    break
                npcalive=0
#end of skeletonroom
#start of dragon room
        if roomroll() == "dragon":   
            clear()
            dragon()
            print("The room ",roommod())
            npchp=draghp
            npchpmax=draghpmax
            npcwepn="HUGE CLAWS"
            npcn="Young Red Dragon"
            npcweph=dragweph
            npcwepl=dragwepl
            npcxp=dragxp
            stund=0
            npcalive=1
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0:
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()
                        print(charn,"Attempts to block!")
                        if stund==0:
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:
                                    spln="fireball"
                                    spldmgl=1
                                    spldmgh=10
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-3
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                            elif cast=="2":
                                clear()
                                if mana >= 5:
                                    heall=2
                                    healh=8
                                    heala=random.randint(heall,healh)
                                    if hp + heala > hpmax:
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()
                        pause=input("Press Enter to continue")
                        clear()
                print("---------------------------------------")
                npcloot=(loot())
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")
                if cont== "2":
                    break
                npcalive=0
#end of dragon room
#start of lich room
        if roomroll() == "lich":   
            clear()
            lich()
            print("The room ",roommod())
            npchp=lichhp
            npchpmax=lichhpmax
            npcwepn="Rotting wand"
            npcn="Undead Lich"
            npcweph=lichweph
            npcwepl=lichwepl
            npcxp=lichxp
            stund=0
            npcalive=1
            #INPUT NPC ABOVE
            while npcalive==1:
                while npchp >0:
                    if hp <=0:
                        print("You have died!")
                        gameover()
                        pause=input()
                        cont=-10
                        break
                    print("---------------------------------------")
                    print(npcn,":\n HP",npchp,"/",npchpmax," DMG",npcwepl,"-",npcweph,)
                    print("---------------------------------------")
                    print(charn,clsn,":\n HP",hp,"/",hpmax," DMG",wepl,"-",weph,)
                    print("---------------------------------------")
                    print("What would you like to do?")
                    print()
                    act1=input("1. Attack 2. Block\n3. Spell  4. Stats ")
                    print()
                    if act1 == "1":
                        clear()
                        dmg=random.randint(wepl,weph)
                        print("You swing your ",wepn," striking the ",npcn," for ",dmg)
                        npchp=npchp-dmg
                        if stund==0:
                            npcdmg=random.randint(npcwepl,npcweph)
                            print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                            hp=hp-npcdmg
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="2":
                        clear()
                        print(charn,"Attempts to block!")
                        if stund==0:
                            blk=random.randint(blkl,blkm)
                            print("The ",npcn," swings at you")
                            npcdmg=random.randint(npcwepl,npcweph)
                            pbdm=npcdmg-blk
                            if pbdm <=0:
                                print("You block all of the attack!")
                            else:
                                print("You resist the attack taking",pbdm,"damage")
                                hp=hp-pbdm
                        if stund!=0:
                            print("The",npcn," is stunned for this turn!")
                            stund=stund-1
                    if act1 =="3":
                        clear()
                        if cls=="2":
                            print("-------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. Fireball:\n   DMG: 1-10             Cost:3 Mana\n2. Heal:\n   HP+: 2-8              Cost:5 Mana \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 3:
                                    spln="fireball"
                                    spldmgl=1
                                    spldmgh=10
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-3
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                            elif cast=="2":
                                clear()
                                if mana >= 5:
                                    heall=2
                                    healh=8
                                    heala=random.randint(heall,healh)
                                    if hp + heala > hpmax:
                                        hp = hpmax
                                    else:
                                        hp = hp + heala
                                    print("You restore ",heala,"HP.")
                                    mana=mana-5
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    nomana()
                        if cls=="1":
                            print("---------------------------------------")
                            print("You currently have",mana,"/",manamax," Mana.")
                            print("What spell would you like to cast?")
                            print("1. QuickSlash:\n   DMG: 2-4                Cost:1 Mana\n2. Shield Bash:\n   DMG: 1-4 50%StunChance  Cost:2 Mana\n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            clear()
                            if cast=="1":
                                if mana >= 1:
                                    spln="quickslash"
                                    spldmgl=2
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    mana=mana-1
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                            if cast=="2":
                                if mana >=2:
                                   spln="Shield bash"
                                   spldmgl=2
                                   spldmgh=4
                                   spldmg=random.randint(spldmgl,spldmgh)
                                   stund=random.randint(0,1)
                                   mana=mana-2
                                   if stund==1:
                                       print("You ",spln," the",npcn,"for",spldmg,"and stunned them!")
                                       npchp=npchp-spldmg
                                   else:
                                       print("You ",spln," the",npcn,"for",spldmg,"and failed to stun them!")
                                       npchp=npchp-spldmg
                                       npcdmg=random.randint(npcwepl,npcweph)
                                       print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                       hp=hp-npcdmg
                        if cls=="3":
                            print("---------------------------------------")
                            print("You currently have",hp,"/",hpmax," HP.")
                            print("What spell would you like to cast?")
                            print("1. Bloody Swipe:\n   DMG:3-18                  Cost:5 HP \n2. Bloodpact:\n   DMG: 0-4 (IF DMG>=3 HP+10)Cost:5 HP \n3. Back")
                            print("---------------------------------------")
                            cast=input()
                            if cast=="1":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloody Swipe"
                                    spldmgl=3
                                    spldmgh=18
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                    npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                                else:
                                    print("NOT NUFF HP")
                            if cast=="2":
                                if hp>5:
                                    hp=hp-5
                                    spln="Bloodpact"
                                    spldmgl=0
                                    spldmgh=4
                                    spldmg=random.randint(spldmgl,spldmgh)
                                    if spldmg >= 3:
                                        hp=hp+10,hpmax
                                        print("You cast ",spln," hitting the",npcn,"for",spldmg,)
                                        npchp=npchp-spldmg
                                    if stund==0:
                                        npcdmg=random.randint(npcwepl,npcweph)
                                        print("The ",npcn," swings their ",npcwepn," striking you for",npcdmg)
                                        hp=hp-npcdmg
                                    if stund!=0:
                                        print("The",npcn," is stunned for this turn!")
                                        stund=stund-1
                    if act1 == "4":
                        clear()
                        stats()
                        pause=input("Press Enter to continue")
                        clear()
                print("---------------------------------------")
                npcloot=(loot())
                print("The ",npcn," falls to the floor dead!")
                print("You loot ",npcloot,"silver pieces")
                print("You gain ",npcxp,"XP!")
                print("Do you continue deeper or leave for the town?")
                print()
                xp=npcxp+xp
                coins=coins+npcloot
                cont=input("1. Continue, 2. Leave")
                if cont== "2":
                    break
                npcalive=0
#end of lich room






