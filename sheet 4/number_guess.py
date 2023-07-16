from random import randint
print("I've thought of a random number between 1 and 1000")
print()

while True:
    number = randint(1,1000)
    answer = input("Guess what that number is! ")
    answer= int(answer)
    if answer < number :
        print("Your guess was too low!")
        print()
    else:
        print("Your guess was too high")
        print()