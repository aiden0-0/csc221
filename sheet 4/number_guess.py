from random import randint

def guessing_game():
    print("I've thought of a random number between 1 and 1000")
    print()
    guess=0
    number = randint(1,1000)
    while True:
        answer = int(input("Guess what that number is! "))
        if answer<number:
            guess = guess+1
            print("Too low!")
            print()
        elif answer>number:
            guess = guess+1
            print("Too high!")
            print()
        else:
            guess = guess+1
            print("You got it!")
            print()
            break
    print("Your number of guesses was " + str(guess))
    print()

    playagain = input("Would you like to play again? ")
    if playagain == "yes":
        print()
        guessing_game()

guessing_game()