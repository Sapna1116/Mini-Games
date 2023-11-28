import random
import pygame
import time

class RockPaperScissors:
    def __init__(self):
        self.list_of_choices = ['ROCK', 'PAPER', 'SCISSORS']
        self.round_counter = 0
        self.max_rounds = 5  # Maximum rounds set to 5
        self.your_score = 0
        self.opponent_score = 0
        self.score_table = {}
        self.difficulty_level = 'Easy'  # Default difficulty level is Easy
        # Initialize pygame mixer for sound effects
        pygame.mixer.init()
        self.win_sound = pygame.mixer.Sound('Refreshed\\win_sound.wav.wav')  
        self.lose_sound = pygame.mixer.Sound('Refreshed\\lost_sound.wav.ogg')
        self.tie_sound = pygame.mixer.Sound('Refreshed\\tie_sound.wav.wav')  


    def game_start(self):
        # Main game loop
        print("\033[38;2;128;0;128mWelcome to the game 'Rock-Paper-Scissors'\033[0m\n")
        while True:
            print("\n\033[95mMENU:\033[0m")
            print("1. Start game")
            print("2. View rules")
            print("3. Change difficulty level")
            print("4. Display difficulty level")
            print("5. Display scoreboard")
            print("6. Exit")

            choice = self.get_user_input("\nEnter your choice (1/2/3/4/5/6/\"exit\"): ", [1, 2, 3, 4, 5, 6])

            if choice == 1:
                if self.round_counter == 0:  
                    self.your_score = 0
                    self.opponent_score = 0
                    self.score_table.clear()
                self.play_with_computer()
            elif choice == 2:
                self.display_rules()
            elif choice == 3:
                self.change_difficulty_level()
            elif choice == 4:
                self.display_difficulty_level()
            elif choice == 5:
                self.display_scoreboard()
            elif choice == 6:
                print("\033[38;2;128;0;128mExiting the game. Thank you for playing!\033[0m")  # Purple text for exit message
                break
            else:
                print("\033[1;31mInvalid choice. Please enter a number between 1 and 6.\033[0m")  # Red text for error


    def display_rules(self):
        print("\033[94m----------------------- \033[95mThe RULES of the game are like\033[94m -------------------------\033[0m")
        print("Between 'Rock' and 'Paper': \"PAPER Wins\" ")
        print("Between 'Paper' and 'Scissors': \"SCISSORS Wins\" ")
        print("Between 'Rock' and 'Scissors': \"ROCK Wins\" ")
        print("\033[94m--------------------------------------------------------------------------------\033[0m")


    def display_difficulty_level(self):
        # Display the current difficulty level
        print(f"\n\033[38;2;128;0;128mCurrent Difficulty Level:\033[0m {self.difficulty_level}")


    def change_difficulty_level(self):
        difficulty_choices = ['Easy', 'Medium', 'Hard']
        print("\nChoose Difficulty Level:")
        for i, level in enumerate(difficulty_choices, start=1):
            print(f"{i}. {level}")

        level_choice = self.get_user_input("\nEnter your choice (1/2/3): ", [1, 2, 3])
        self.difficulty_level = difficulty_choices[level_choice - 1]
        print(f"Difficulty level set to: {self.difficulty_level}")


    def get_user_input(self, prompt, valid_range):
        while True:
            try:
                user_input = input(prompt)
                if user_input.lower() == 'exit':
                    exit()
                user_input = int(user_input)
                if user_input in valid_range:
                    return user_input
                else:
                    print(f"\033[1;31mInvalid input. Please enter a number between {valid_range[0]} and {valid_range[-1]}.\033[0m")  # Red text for error
            except ValueError:
                print("\033[1;31mInvalid input. Please enter a valid number.\033[0m")  # Red text for error


    def play_with_computer(self):
        self.round_counter += 1
        your_choice = self.get_user_input("Enter your choice from the options - \"Rock/Paper/Scissors\" - (1/2/3/\"exit\"): ", valid_range=[1, 2, 3])

        # Updated: Generate opponent choice based on difficulty level
        opponent_choice = self.generate_opponent_choice()
        self.evaluate_choices(your_choice, opponent_choice)


    def generate_opponent_choice(self):
        if self.difficulty_level == 'Easy':
            return random.randint(1, 3)  # Random choice with equal probability
        elif self.difficulty_level == 'Medium':
            # Slightly biased towards a specific choice
            return random.choices([1, 2, 3], weights=[0.2, 0.5, 0.3])[0]
        elif self.difficulty_level == 'Hard':
            opponent_choice = self.generate_hard_opponent_choice([])
            return opponent_choice


    def generate_hard_opponent_choice(self, your_choices):
        # If the player has made at least one move
        if your_choices:
            # Counter the player's last move
            last_player_move = your_choices[-1]
            # Basic strategy: Counter by choosing the winning move against the player's last move
            counter_moves = {1: 3, 2: 1, 3: 2}
            return counter_moves[last_player_move]
        else:
            return random.randint(1, 3)


    def evaluate_choices(self, your_choice, opponent_choice):
        if 1 <= your_choice <= 3 and 1 <= opponent_choice <= 3:
            time.sleep(0.5) 
            print("\nYou chose:")
            self.display_choice(your_choice)
            print("\nOpponent is deciding... ", end='', flush=True)  # Print countdown horizontally
            time.sleep(0.2)  

            for i in range(3, 0, -1):
                time.sleep(0.2)  # Short delay between countdown

            print("\nOpponent chose:")
            self.display_choice(opponent_choice)
            print("--------------------------------------------------------")
            time.sleep(1)  # Short delay before printing result

            if your_choice == opponent_choice:
                print("\033[1;33m-----It's a TIE!!------\033[0m")  # Yellow text for tie
                self.tie_sound.play()  # Play tie sound effect
            elif (your_choice - opponent_choice) % 3 in [1, -2]:
                print("\033[1;32m-----You WIN!!------\033[0m")  # Green text for win
                self.win_sound.play()  # Play win sound effect
                self.your_score += 1
            else:
                print("\033[1;31m-----Opponent WINS!!------\033[0m")  # Red text for loss
                self.lose_sound.play()  # Play lose sound effect
                self.opponent_score += 1

            # Add scores to the score table
            self.score_table[self.round_counter] = {'Your Score': self.your_score, 'Opponent\'s Score': self.opponent_score}

            # Display scoreboard automatically after 5 rounds
            if self.round_counter%5 == 0:
                self.round_counter == 0  # Reset scores if starting a new game
                time.sleep(1) 
                self.display_scoreboard()
                time.sleep(0.8) 
                self.game_over_message()
                time.sleep(1.0) 

        else:
            print(f"\n\033[1;31m!!!!Wrong Input, Please enter a number between {1} and {3}!!!!\033[0m")  # Red text for error
        print("========================================================")


    def display_choice(self, choice):
        # Simple ASCII art for each choice with brown-like color
        if choice == 1:
            print("\033[38;2;139;69;19m   _______\033[0m")
            print("\033[38;2;139;69;19m---      \\\033[0m")
            print("\033[38;2;139;69;19m   (ROCK)\033[0m")
            print("\033[38;2;139;69;19m    \______)\033[0m")
        elif choice == 2:
            print("\033[38;2;139;69;19m   _______\033[0m")
            print("\033[38;2;139;69;19m---      \\\033[0m")
            print("\033[38;2;139;69;19m   (PAPER)\033[0m")
            print("\033[38;2;139;69;19m    \______)\033[0m")
        elif choice == 3:
            print("\033[38;2;139;69;19m   _______\033[0m")
            print("\033[38;2;139;69;19m---      \\\033[0m")
            print("\033[38;2;139;69;19m   (SCISSORS)\033[0m")
            print("\033[38;2;139;69;19m    \______)\033[0m")


    def display_scoreboard(self):
        print("\n\033[95mSCOREBOARD:\033[0m")  
        print("\033[94m-------------------------------------------------------------------------\033[0m")  
        print("| {:^5} | {:^24} | {:^27} |".format("\033[94mRound\033[0m", "\033[94mYour Score\033[0m", "\033[94mOpponent's Score\033[0m"))
        print("\033[94m-------------------------------------------------------------------------\033[0m")
        for round_num, scores in self.score_table.items():
            print("| {:^5} | {:^15} | {:^18} |".format(round_num, scores['Your Score'], scores['Opponent\'s Score']))
        print("\033[94m-------------------------------------------------------------------------\033[0m") 


    def game_over_message(self):
        if self.your_score > self.opponent_score:
            print("\033[1;32mCongratulations! You won the game!\033[0m")  # Green text for win
            self.win_sound.play()  # Play win sound effect
        elif self.your_score < self.opponent_score:
            print("\033[1;31mOops! You lost the game. Better luck next time!\033[0m")  # Red text for loss
            self.lose_sound.play()  # Play lose sound effect
        else:
            print("\033[1;33mIt's a tie game. Well played!\033[0m")  # Yellow text for tie
            self.tie_sound.play()  # Play tie sound effect for a tie game
        self.score_table.clear()
        self.your_score = 0
        self.opponent_score = 0


if __name__ == "__main__":
    game = RockPaperScissors()
    game.game_start()
