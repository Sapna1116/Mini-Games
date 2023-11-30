import random as r

center = 5
edge = [2, 4, 6, 8]
corner = [1, 3, 7, 9]

def showBoard() :
    print(("_"+ board[1]+ "_|") + ("_"+ board[2]+ "_|") + ("_"+ board[3]+ "_"))
    print(("_"+ board[4]+ "_|") + ("_"+ board[5]+ "_|") + ("_"+ board[6]+ "_"))
    print((" "+ board[7]+ " |") + (" "+ board[8]+ " |") + (" "+ board[9]+ " "))

#def isBoardFull2() :
#    for i in range(1,11) :
#       if (board[i] == "X" or board[i] == "x" or board[i] == "O" or board[i] == "o") :
#           return True
#       else :
#           return False

def isBoardNotFull() :
    y = board.count(' ') 
    if (y < 1) :
        return False
    else :
        return True

def isFreeSpace(pos) :
    if (board[pos] == " ") :
        return True
    else:
        return False

def insertSymbol(pos,letter) :
    board[pos] = letter

def isWinner(sym) :
    if ((board[1]==board[2]==board[3]==sym) or 
    (board[4]==board[5]==board[6]==sym) or 
    (board[7]==board[8]==board[9]==sym) or 
    (board[1]==board[4]==board[7]==sym) or 
    (board[2]==board[5]==board[8]==sym) or 
    (board[3]==board[6]==board[9]==sym) or 
    (board[1]==board[5]==board[9]==sym) or 
    (board[3]==board[5]==board[7]==sym)) :
        return True
    else :
        return False


def playerMove(symbol, b, n1) :
    move = True
    while (move) :
        possiblePlaces = [i for i in range(1,10) if b[i]==" " ]
        print(f"Possible places in {n1}'s chance : ", possiblePlaces)

        if len(possiblePlaces) == 0 :
            move = False
        else :
            try :
                pos = int(input(f"Choose a position {n1} (Range:1-9):"))
                if type(pos) == int :
                    if (pos>0 and pos<10) :         
                        if(isFreeSpace(pos)) :
                            insertSymbol(pos,symbol)
                            move = False
                        else :
                            print("\n\tSorry! This space is occupied!\tChoose another space!\n")
                    else :
                        print("\n\tChoose a place from the possible range only!\n")
            except :
                print("Choose an integer from 1-9!")

def compMove(s2, s1, b) :
    move = True
    while(move) :
        possiblePlaces = [i for i in range(1,10) if b[i]==" " ]
        print("Possible places in computer's chance : ", possiblePlaces)

        if len(possiblePlaces) == 0 :
            isBoardNotFull == False
            move = False

        else :
            if len(possiblePlaces) == 8 :   #It's the 1st move for comp
                for i in range(1,10) :
                    if s1 == b[i] and i == center:
                        pos = r.choice(corner)
                        insertSymbol(pos, s2)
                        move =False
                        break

                    elif s1 == b[i] and (i in corner or i in edge) :
                    # OR elif s1 == b[i] and i != center :
                        pos = center
                        insertSymbol(pos, s2)
                        move =False
                        break
        
            else :
                for i in possiblePlaces :
                    insertSymbol(i,s2) 
                    if isWinner(s2) :
                        insertSymbol(i,s2)
                        move = False
                        break
                    else :
                        insertSymbol(i," ")

                if move != False :
                    for i in possiblePlaces :
                        insertSymbol(i,s1) 
                        if isWinner(s1) :
                            insertSymbol(i,s2)
                            move = False
                            break
                        else :
                            insertSymbol(i," ")

                    if move != False :
                        for i in possiblePlaces:
                            if i == 5 :
                                insertSymbol(5,s2)
                                move = False
                                break
                            else :
                                if i in corner :
                                    pos = r.choice([j for j in corner if j in possiblePlaces])
                                    insertSymbol(pos, s2)
                                    move = False
                                    break 
                                else :
                                    pos = r.choice([j for j in edge if j in possiblePlaces])
                                    insertSymbol(pos, s2)
                                    move = False
                                    break 

def friendMove(symbol, b, n2) :
    move = True
    while (move) :
        possiblePlaces = [i for i in range(1,10) if b[i]==" " ]
        print(f"Possible places in {n2}'s chance : ", possiblePlaces)

        if len(possiblePlaces) == 0 :
            move = False
        else :
            try :
                pos = int(input(f"At which position {n2} want to insert the selected symbol? (Range:1-9):"))
                if type(pos) == int :
                    if (pos>0 and pos<10) :         
                        if(isFreeSpace(pos)) :
                            insertSymbol(pos,symbol)
                            move = False
                        else :
                            print("\n\tSorry! This space is occupied!\tChoose another space!\n")
                    else :
                        print("\n\tChoose a place from the possible range only!\n")
            except :
                print("Choose an integer from 1-9!")

def main(opponent, n1, n2) :       
    print("----------------WELCOME to the game TIC-TAC-TOE----------------")
    showBoard()
    sym = input(f"Which symbol would {n1} like to play with? ('x' or 'o') :")
    if sym.lower()=="x" :
        symbol1 = "x"
        symbol2 = "o"
        print(f"{n1} chose :", symbol1)
        print(f"{n2} got :", symbol2)
    else :
        symbol1 = "o"
        symbol2 = "x"
        print(f"{n1} chose :", symbol1)
        print(f"{n2} got :", symbol2)

    while isBoardNotFull() : 
        possiblePlaces = [i for i in range(1,10) if board[i]==" " ]
        if len(possiblePlaces) == 0 :
            print("It's a TIE!! \n Exiting")
            break
            
        else :
            if not(isWinner(symbol2)) :
                playerMove(symbol1, board, n1)
                showBoard()
                print("-----------------------------------------------")  
            else :
                print(f"Ohhhh! {n1} Lost to {n2} !!!")
                break

            possiblePlaces = [i for i in range(1,10) if board[i]==" " ]
            if  len(possiblePlaces) != 0 :
                if not(isWinner(symbol1)) :
                    if opponent == 1 :
                        compMove(symbol2, symbol1, board)
                        showBoard()
                        print("-----------------------------------------------")
                    elif opponent == 2 :
                        friendMove(symbol2, board, n2)
                        showBoard()
                        print("-----------------------------------------------")  

                else :
                    print(f"Hurray! {n1} Won against {n2} !!!")
                    break

while(True) :
    ch = input("Do your want to play the game ?(Y/y for yes) : ")
    if ch.lower()=="y" :
        opponent = int(input("Whom do you want to play with - 1)the computer    or   2) your friend ?? : "))
        if opponent == 1 :
            name1 = input("Enter your name : ")
            board = [" " for i in range(1,11)]
            main(opponent, name1, "Computer")
        elif opponent == 2 :
            name1 = input("Enter your name : ")
            name2 = input("Enter your friend's name : ")
            board = [" " for i in range(1,11)]
            main(opponent, name1, name2)
        else :
            print("Wrong Choice !!!")

    else :
        print("Exiting the Game!")
        break