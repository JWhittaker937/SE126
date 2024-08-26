#Name Jared Whittaker
#Lab # 5 Theater Problem   
#Date 08/26/2024 
#Lab Description
#Variable Dictionary-------------------------------------
rowselection=0
seatselection=0
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
row6=[]
row7=[]
row8=[]
row9=[]
row10=[]
row11=[]
row12=[]
row13=[]
row14=[]
row15=[]
row16=[]
row17=[]
row18=[]
row19=[]
row20=[]
row21=[]
row22=[]
row23=[]
row24=[]
row25=[]
row26=[]
row27=[]
row28=[]
row29=[]
row30=[]
#Imports-------------------------------------------------
#Functions-----------------------------------------------
#Main Code-----------------------------------------------
for i in range(0,15):
    row1.append("X")
    row2.append("X")
    row3.append("X")
    row4.append("X")
    row5.append("X")
    row6.append("X")
    row7.append("X")
    row8.append("X")
    row9.append("X")
    row10.append("X")
    row11.append("X")
    row12.append("X")
    row13.append("X")
    row14.append("X")
    row15.append("X")
    row16.append("X")
    row17.append("X")
    row18.append("X")
    row19.append("X")
    row20.append("X")
    row21.append("X")
    row22.append("X")
    row23.append("X")
    row24.append("X")
    row25.append("X")
    row26.append("X")
    row27.append("X")
    row28.append("X")
    row29.append("X")
    row30.append("X")
print(f"[{"Row":3}]  {" A ":3}{" B ":3}{" C ":3}{" D ":3}{" E ":3}{" F ":3}{" G ":3}{" H ":3}  |  |  {" I ":3}{" J ":3}{" K ":3}{" L ":3}{" M ":3}{" N ":3}{" O ":3}{" P ":3}{" Q ":3}{" R ":3}{" S ":3}{" T ":3}{" U ":3}  |  |  {" V ":3}{" W ":3}{" X ":3}{" Y ":3}{" Z ":3}{" 1 ":3}{" 2 ":3}{" 3 ":3}{" 4 ":3}")
for i in range(0,len(row1)):
    print(f"[{i+1:3}]\t{row1[i]:3}{row2[i]:3}{row3[i]:3}{row4[i]:3}{row5[i]:3}{row6[i]:3}{row7[i]:3}{row8[i]:3} |  |   {row9[i]:3}{row10[i]:3}{row11[i]:3}{row12[i]:3}{row13[i]:3}{row14[i]:3}{row15[i]:3}{row16[i]:3}{row17[i]:3}{row18[i]:3}{row19[i]:3}{row20[i]:3}{row21[i]:3} |  |   {row22[i]:3}{row23[i]:3}{row24[i]:3}{row25[i]:3}{row26[i]:3}{row27[i]:3}{row28[i]:3}{row29[i]:3}{row30[i]:3}")

rowselection=int(input(f"What row number would you like to select?"))
if rowselection >= 1 and rowselection<= 5:
    print(f"Row {rowselection} costs $200 per seat.")
elif rowselection >5 and rowselection <= 10:
    print(f"Row {rowselection} costs $175 per seat.")
elif rowselection >10 and rowselection <= 15:
    print(f"Row {rowselection} costs $150 per seat.")
