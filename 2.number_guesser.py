import random

top_of_range =  input("Type a number: ")

# .isdigit() check it is number
if top_of_range.isdigit():

    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)
# randrange doesn't include 11
# randint include 11
number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        # Continue bring back to top of the loop
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Too high")
    else:
        print("Too low")

# , 는 + 랑 다르게 뛰어쓰기가 자동
print("you got in in", number_of_guesses, "guesses")