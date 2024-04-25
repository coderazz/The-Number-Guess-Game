import random
def Easy():
    x = random.randint(1,10)
    
    while True:
        numguess = input("What number of Guesses would you like to play with: ")
        if not numguess.isdigit():
            print("Input an Integer")
            continue
        numguess = int(numguess)
        break

    
    for i in range(1,numguess + 1):  #range functions for the number of iterations, with + 1 because computers counts from 0
    #for reference try: for i in range(1, 10):, print i , will counts from 1-9, so a + 1 was needed to complete the cycle!
            guess = input("let's play the guess game (1-10), pick a lucky number (guess {} of {}) ".format(i,numguess))
            print("remember you can make 5 lucky guess")

            if not guess.isdigit():
                print("please enter a number")
                continue
            guess = int(guess)  #type casting
    
            if guess < 1 or guess > 10:
                print("make a guess btw 1 and 10") 
                continue

            elif guess < x:
                print("Your Guess is Lesser Than the correct Number, Try Again")

            elif guess > x:
                print("Your Guess is Greater Than the correct Number, Try Again")


            elif guess == x:
                print("congratulations, you got it")
                break
        
            else:
                print("sorry, you're not lucky today, try again")
        
    print("correct guess is " + str(x))


def Medium():
     x = random.randint(1,15)
     while True:
        numguess = input("What number of Guesses would you like to play with: ")
        if not numguess.isdigit():
                print("Input an Integer")
                continue
        numguess = int(numguess)
        break
    
     for i in range(1,numguess + 1):  #range functions for the number of iterations, with + 1 because computers counts from 0
    #for reference try: for i in range(1, 10):, print i , will counts from 1-9, so a + 1 was needed to complete the cycle!
            guess = input("let's play the guess game (1-15), pick a lucky number (guess {} of {}) ".format(i,numguess))
            print("remember you can make 5 lucky guess")

            if not guess.isdigit():
                print("please enter a number")
                continue
            guess = int(guess)  #type casting
    
            if guess < 1 or guess > 15:
                print("make a guess btw 1 and 15") 
                continue

            if guess < x:
                print("Your Guess is Lesser Than the correct Number, Try Again")

            if guess > x:
                print("Your Guess is Greater Than the correct Number, Try Again")


            if guess == x:
                print("congratulations, you got it")
                break
        
            else:
                print("sorry, you're not lucky today, try again")
        
     print("correct guess is " + str(x))

def Hard():
     x = random.randint(1,20)
     while True:
        numguess = input("What number of Guesses would you like to play with: ")
        if not numguess.isdigit():
                print("Input an Integer")
                continue
        numguess = int(numguess)
        break
    
     for i in range(1,numguess + 1):  #range functions for the number of iterations, with + 1 because computers counts from 0
    #for reference try: for i in range(1, 10):, print i , will counts from 1-9, so a + 1 was needed to complete the cycle!
            guess = input("let's play the guess game (1-20), pick a lucky number (guess {} of {}) ".format(i,numguess))
            print("remember you can make 5 lucky guess")

            if not guess.isdigit():
                print("please enter a number")
                continue
            guess = int(guess)  #type casting
    
            if guess < 1 or guess > 20:
                print("make a guess btw 1 and 20") 
                continue

            if guess < x:
                print("Your Guess is Lesser Than the correct Number, Try Again")

            if guess > x:
                print("Your Guess is Greater Than the correct Number, Try Again")


            if guess == x:
                print("congratulations, you got it")
                break
        
            else:
                print("sorry, you're not lucky today, try again")
        
     print("correct guess is " + str(x))



while True:
    print("Welcome To The Guess Game")
    print("please, Select your difficulty Level")
    print("1. Easy: 1-10")
    print("2. Medium: 1-15")
    print("3. Hard: 1-20")

    Level = input("Select from the list: ")

    if not Level.isdigit():
        print("invalid choice")
        continue
    
    Level = int(Level)

    if Level > 3 or Level < 1:
        print("choose btw 1 and 3")
        continue

    elif Level == 1:
        print("Easy")
        Easy()

    elif Level == 2:
        print("Medium")
        Medium()

    elif Level == 3:
        print("Hard")
        Hard()
