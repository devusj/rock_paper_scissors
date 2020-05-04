import random

user_choice = 0
computer_choice = 0

def choose_option():
    user_choice = input("Choose between Rock, Paper, Scissors: ")
    user_choice = user_choice.lower()
    if user_choice == "rock":
        user_choice = "r"
    elif user_choice == "paper":
        user_choice = "p"
    elif user_choice == "scissors":
        user_choice = "s"
    else:
        print("Invalid choice, choose again: ")
        choose_option()
    return user_choice


def computer_option():
    computer_choice = random.randint(0,2)
    if computer_choice == 0:
        computer_choice = "r"
    elif computer_choice == 1:
        computer_choice = "p"
    elif computer_choice == 2:
        computer_choice = "s"
    else:
        print("error")
    return computer_choice

while True:
    userchoice = choose_option()
    computer_choice = computer_option()vush
    if userchoice == computer_choice:
        print("Its a tie, please try again! ")
    elif userchoice == "r" and computer_choice == "p":
        print("You loose, sucker!")
    elif userchoice == "p" and computer_choice == "s":
        print("You loose, sucker!")
    elif userchoice == "s" and computer_choice == "r":
        print("You loose, sucker!")
    elif userchoice == "r" and computer_choice == "s":
        print("You win, Legend!")
    elif userchoice == "p" and computer_choice == "r":
        print("You win, Legend!")
    elif userchoice == "s" and computer_choice == "r":
        print("You win, Legend!")
    else:
        print("Error")

    repeat_game = input("Would you like to play again? ")
    repeat_game = repeat_game.lower
    if repeat_game == "yes":
        pass
    elif repeat_game == "no":
        print("See you next time!")
        break
    else:
        print("error")



