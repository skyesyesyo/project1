import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors (r,p,s) or Q to quit: ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # Rock:0, Paper: 1, Sissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" or "r" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" or "p" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" or "s" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins,"times.")
print("Computer won", computer_wins,"times.")

print("Goodbye!")