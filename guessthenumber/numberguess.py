import random

number = random.randint(1,10)
tries = 0
win = False


name = input("Hello, What is your username?")

print("Hello", name + ".", )

question = input("Would you like to play a game? [Y/N]")
if(question.lower() == "n"):
    print("Oh..okay")
    exit()

if(question.lower() == "y"):
    print("I'm thinking of a number between 1 & 10")
while not win:
    guess = int(input("Have a guess: "))
    tries += 1
    if(guess == number):
        win = True
    elif(guess < number):
        print("Guess higher")
    elif(guess > number):
        print("Guess lower..")

print("Congrats, you guessed correctly. The number was indeed {}".format(number))
print("it had taken you {} tries".format(tries))



