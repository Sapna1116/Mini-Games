import random as r
import re

h_movie_list = ["Avengers Endgame", "jumanji welcome to the jungle", "Anabelle Comes Home", "The Twilight Saga", "The Croods", "The Conjuring 2", "Birds of Prey", " Sonic the Hedgehog", "Inception", "DeadPool"]
b_movie_list = ["Chennai Express", "Hera Pheri", "Ramya Vastavaya", "Student Of The Year 2", "Singh Is Kinng", "Jab We Met", "Ghost Stories", "Chandni Chowk to China", "Uri The Surgical Strike", "Luka Chuppi"]
game_list = ["Tug of War", "Hopscotch", "Hide and Seek", "Softball", "Soccer", "Table Tennis", "Snakes And Ladders", "Solitaire", "Free Fire", "Rugby"]
tech_list = ["Artificial Intelligence", "Machine Learning", "Data Analytics", "Web Development", "Cyber Security", "Digital Marketing", "DevOps", "Internet Of Things", "Cloud Computing", "Software Development"]
animal_list = ["Chimpanzee", "Beaver", "Llama", "Rhinoceros", "Hippopotamus", "Reindeer", "Antelope", "Porcupine", "Black Buck", "Lobster"]
bird_list =["Ostrich", "Falcons", "Humming Bird", "Albatross", "Canary", "Chikadee","Flamingo", "Heron", "Nightingale", "Macaw"]

def choose_word(l) :
    return r.choice(l).lower()

def hangman(i) :
    if i == 9 :
        print("""   -------   """)
    elif i == 8 :
        print("""   -------   
    
     O """)
    elif i == 7 :
        print("""   -------   
     
     O
     | """)
    elif i == 6 :
        print("""   -------   
     
     O
     |
    /  """)
    elif i == 5 :
        print("""   -------   
     
     O
     |
    / \ """)
    elif i == 4 :
        print("""   -------   
     
    \O
     |
    / \ """)
    elif i == 3 :
        print("""   -------   
     
    \O/
     |
    / \ """)
        print("!!!!!!!!!!!!You can do it!!!!!!!!!!!!".upper())
    elif i == 2 :
        print("""   -------   
       |
    \O/
     |
    / \ """)
        print("!!!!!!!!!!!!Save this man, It's life is in your hands!!!!!!!!!!!!".upper())
    elif i == 1 :
        print("""   -------   
       |
    \O/|
     |
    / \ """)
        print("!!!!!!!!!!!!It's his last chance to live!!!!!!!!!!!!".upper())
    elif i == 0 :
        print("""   -------   
       |
     O_|
    /|\ 
    / \ """)
        print("!!!!!!!!!!!!Alas!!! You let the poor man die!!!!!!!!!!!!".upper())
        print("""> <
 .
 U""")
        print("The word was : ", word)
        return i
        

def checking_the_letter(word) :
    n_of_chances = 10
    already_guessed = l = []
    new_l = ""

    for i in range(len(word)) :
        if " " in word[i] :
            new_l = new_l + "  "
        else :
            new_l = new_l + "_ "
    print(new_l)
    
    for i in range(len(word)) :
        if " " in word[i] :
            l.append(" ")
        else :
            l.append("_ ")

    while n_of_chances > 0 :
        for i in range(len(word)) :
            if " " in word[i] :
                l[i] = " "
                new_l = ""
                for i in range(len(word)) :
                    new_l = new_l + l[i]

            else :          
                print("----------------------------------------------------------------------------")  
                letter = input("Guess the letter : ")              
                if (letter in word) :
                    if (letter not in already_guessed) :
                        already_guessed.append(letter)
                        result = [i for i in range(len(word)) if word.startswith(letter, i)]
                        for j in result :
                            l[j] = letter
                        new_l = ""
                        for i in range(len(word)) :
                            new_l = new_l + l[i]
                        print(new_l)
                    
                    else: 
                        print("This letter's all occurances had already been inserted.  Choose a letter again") 

                    if new_l == word :     
                        print("You are a saviour!!!!You are a hero for this man!".upper())
                        n_of_chances = 0
                        break

                elif letter not in word :
                    
                    print("This letter is not present in the word!! ")
                    print("  You lost 1 chance")
                    n_of_chances -= 1
                    print(f"No. of chances left : {n_of_chances}")
                    i = hangman(n_of_chances)
                    if i == 0 :
                        break
                           
def wannaPlay() :
    ch = input("Do you want to play again??(Y/y) : ")
    if ch.lower() == "y" :
        move = "y"
        return move
    else :
        move = "n"
        return move


print("--------------------------------------Welcome to the game \"HANGMAN\" ---------------------------------------")

move = input("Do you want to check the instructions ?? (Y/y) : ")
if move.lower()=='y':
    print("\nPoints to remember :")
    print("\n\t1)You will get 10 chances to guess the word ")
    print("\n\t2)You will loose 1 chance for every incorrect word you will guess!")
    print("\n\t3)You can guess only 1 letter in 1 chance")
    print("\n\t4)Spaces present in the word has already been filled ")
    print("\n\t5)Special characters have been ignored for your ease")
    print("\n\t6)Don't worry about the capital and small letters in the word")
    print("\n\tTry your best to save the innocent man !!!!")
    print("\nHINT ==> You check the possibility for a vowel")


print("\nYou can choose the category from which you would like to choose a word! - ")
print("[1]'Hollywood movie names'\t[2]'Bollywood movie names'\t[3]'Name of games'\n[4]'Technical words'\t[5]'Animal names'\t[6]'Birds names'")

move = input("Ready to play the game ?? (Y/y) : ")
while move.lower() == "y" :
    try :
        choice = int(input("\n From which category would you like to choose a word ? (1-6): "))
        if type(choice)==int :
            while (choice in range(1,7)) :
                if choice==1 :
                    word = choose_word(h_movie_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                elif choice==2 :
                    word = choose_word(b_movie_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                elif choice==3 :
                    word = choose_word(game_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                elif choice==4 :
                    word = choose_word(tech_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                elif choice==5 :
                    word = choose_word(animal_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                elif choice==6 :
                    word = choose_word(bird_list)
                    checking_the_letter(word)
                    move = wannaPlay()
                    break
                else :
                    print("Wrong Choice!!! Choose from (1-6) only")
            else :
                print("Choose Again from (1-6) only")
    except :
        print("Choose an integer value from (1-6) ")
else :  
    print("Exiting the game!!")


