import random

secret_number = random.randint(1,10)

guess_the_number = 0
print("Guess the number from 1 to 10")

#While condition will terminate if the condition is True
while guess_the_number != secret_number:
    #Input the number which is guessed
    guess_the_number = int(input("Enter your Guess: "))

    #if condition will terminate if the secret number is found from the range
    if guess_the_number < secret_number:
        print("The number you guessed is Too Low")
    elif guess_the_number > secret_number:
        print("The number you guessed is Too High")
    else:
        print("Congratulations! You Guessed Correct")


