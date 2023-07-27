import random #random for computer choice
import time #time for typing eefect on welcome message
from colorama import init, Fore #color for colured text

init(autoreset=True)

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").lower()# lower case to make case insensitve
        if user_choice in ['r', 'p', 's']:
            return user_choice
        else:
            print(Fore.RED + "Invalid choice. Please enter R, P, or S.")

def get_computer_choice():
    return random.choice(['r', 'p', 's']) #random choice from this

def convert_choice_to_word(choice): #convert singel letter to word
    if choice == 'r':
        return Fore.YELLOW + "rock"
    elif choice == 'p':
        return Fore.BLUE + "paper"
    elif choice == 's':
        return Fore.GREEN + "scissors"

def determine_winner(user_choice, computer_choice):#game rules
    user_choice = user_choice.lower()
    computer_choice = computer_choice.lower()

    if user_choice == computer_choice:
        return "It's a tie!"

    elif (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 'p' and computer_choice == 'r') or \
            (user_choice == 's' and computer_choice == 'p'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():#play game set scores to 0
    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:#while loop for less than 2
        user_choice = get_user_choice()

        if user_choice in ['r', 'p', 's']:
            computer_choice = get_computer_choice()
            print(f"You chose {convert_choice_to_word(user_choice)}, {Fore.LIGHTWHITE_EX} and the computer chose {convert_choice_to_word(computer_choice)}.")
            result = determine_winner(user_choice, computer_choice)
            if "You win" in result:
                print(Fore.GREEN + result)
                user_score += 1
            elif "Computer wins" in result:
                print(Fore.RED + result)
                computer_score += 1
            else:
                print(Fore.YELLOW + result)

        else:
            print(Fore.RED + "Invalid choice. Please enter R, P, or S.")

    if user_score > computer_score:
        print(Fore.GREEN + "Congratulations! You win the best of 3!")
    else:
        print(Fore.RED + "The computer wins the best of 3. Better luck next time!")

def welcome_message():
    message = "Welcome to the Rock-Paper-Scissors game!\n"
    message += "The first player to win 2 rounds out of 3 will be the overall winner.\n"
    for char in message:
        print(Fore.BLUE + char, end='', flush=True) #end`` = ensures that letters are printed on same line
        time.sleep(0.03)  # Adjust the speed at which characters appear (faster typing)
    print()  # Print a newline after the welcome message
welcome_message()

# Run the game
play_game()





