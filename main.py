#put Treasure at some place which is entered by user
# In position first digit shows the column no and second digit shows the row number

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position1=list(position)
#first way to do it
#print(position1)
#a=int(position1[0])-1
#print(a)
#b=int(position1[1])-1
#print(b)
#map[b][a]="x"

#second way to do it
map[int(position1[1])-1][int(position1[0])-1]="x"




print(f"{row1}\n{row2}\n{row3}")
