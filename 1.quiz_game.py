print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

print("Current score = "+ str(score))

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score +=1
    print("Current score = "+ str(score))
else:
    print('Incorrect!')
    print("Current score = "+ str(score))

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('Correct')
    score +=1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score +=1
    print("Current score = "+ str(score))
else:
    print('Incorrect!')
    print("Current score = "+ str(score))

answer = input("What does PS stand for? ")
if answer.lower() == "power supply":
    print('Correct')
    score +=1
    
else:
    print('Incorrect!')
    

print("Your score = "+ str(score))
print("You got "+ str(100*score/4)+"%")