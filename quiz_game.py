print("Welcome to the Quiz Game! ")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    print("Maybe next time! ")
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of India? ")
if answer.lower() == "new delhi":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("What country's capital is Tokyo? ")
if answer.lower() == "japan":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("What country's capital is Rome? ")
if answer.lower() == "italy":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

answer = input("What place is known as the land of cats? ")
if answer.lower() == "istanbul":
    print("Correct! ")
    score += 1
else:
    print("Incorrect!")

print("Thanks for playing! ")

print("Your score is " + str(score) + " out of 5! ")
print("You got " + str((score/5)*100) + "%")
