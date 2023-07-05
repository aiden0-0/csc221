correct_answer = 0
for x in range(10):
    from random import randint
    num1 = randint(1,10)
    num2 = randint(1,10) 
    print()
    print(str(num1) + " times " + str(num2) + " is equal to what?")
    answer = input("Enter a number: ")
    answer = int(answer)
    if answer == num1*num2:
        print()
        print("Good job!")
        correct_answer = correct_answer + 1
    else:
        print()
        print("Good try")
print("There was 10 questions and you got " + str(correct_answer) + " of them right.")
if correct_answer>=8:
    print("Nice job!")
else:
    print("You need to study more")
if correct_answer != 10:
    print()
else:
    print()
    print("Time for the hard questions")
    for x in range(5):
        num3 = randint(1,100)
        num4 = randint(1,100)
        print()
        print(str(num3) + " times " + str(num4) + " is equal to what?")
        wanswer = input("Enter your answer: ")
        wanswer = int(wanswer)
        if wanswer == num3*num4:
            print()
            print("Correct")
            correct_answer = correct_answer+1
        else:
            print()
            print("BOOOOOOO")
    print("Now that you answered these 5 hard questions I will show you the results.")
    print("You got " + str(correct_answer) + " of them total right.")
if correct_answer < 15:
    print("Better luck next time")
else:
    print("Congratulations!!!")
