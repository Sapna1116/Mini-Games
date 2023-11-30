import random as r

box1 =[ '''
         |---------------|
         |               |
         |       o       |
         |               |
         |---------------|''',
       
       '''
         |---------------|
         |               |
         |   o       o   |
         |               |
         |---------------|''',
       
       '''
         |---------------|
         | o             |
         |      o        |
         |           o   |
         |---------------|''',
       
       '''
         |---------------|
         |  o         o  |
         |               |
         |  o         o  |
         |---------------|''',
       
       '''
         |---------------|
         |   o       o   |
         |       o       |
         |   o       o   |
         |---------------|''',
       
       '''
         |---------------|
         |    o     o    |
         |    o     o    |
         |    o     o    |
         |---------------|''']

box2 = [" o ",
        "o  o",
        "o  o  o",
        "o  o\no  o",
        "o   o\n  o  \no   o",
        "o  o\no  o\no  o"]

box = [" " for i in range(1,11)]

def board() :
    print(" --- ")
    print("|"+box[1]+box[2]+box[3]+"|")
    print("|"+box[4]+box[5]+box[6]+"|")
    print("|"+box[7]+box[8]+box[9]+"|")
    print(" --- ")

def val(x) :
    if x==1:
      box[5] = "o" 
      board()       
    if x==2:
      box[4]=box[6]="o"  
      board()    
    if x==3:
      box[1]=box[5]=box[9]="o"      
      board()
    if x==4:
      box[1]=box[3]=box[7]=box[9]="o" 
      board()
    if x==5:
      box[1]=box[3]=box[5]=box[7]=box[9]="o"
      board()
    if x==6:     
      box[1]=box[3]=box[4]=box[6]=box[7]=box[9]="o"   
      board()

choice = input("Do you want to roll the Dice? (Y/y for Yes) : ")

while (choice=="Y" or choice=="y") :
    x = r.randint(1,6)
    #print(box2[x-1],"\n")
    #print(box1[x-1],"\n")
    val(x)
    choice = input("Do you want to roll the dice again? : ")
    for i in range(1,10):
      box[i] = " "
else :
    print("You chose not to roll the dice. Exiting!")


