from random import randint
num1=randint(1,1000)

print("I've thought of a number between 1 and 1000.")
answer = input(print("Guess what it is."))
answer=int(answer)
if answer == num1:
    print("That's the number I was thinking of!")
else:
    print("Try again!")

