import random

x = random.randint(1,10)

numguess = 5 #no of iterations
for i in range(1,numguess + 1):  #range functions for the number of iterations, with + 1 because computers counts from 0
#for reference try: for i in range(1, 10):, print i , will counts from 1-9, so a + 1 was needed to complete the cycle!
    guess = input("let's play a a guess game, pick a lucky (guess {} of {}) ".format(i,numguess))
    print("remember you can make 5 lucky guess")

    if not guess.isdigit():
        print("please enter a number")
        continue
    guess = int(guess)  #type casting
    
    if guess < 1 or guess > 10:
        print("make a guess btw 1 and 10") 
        continue
    if guess == x:
        print("congratulations, you got it")
        break
    else:
        print("sorry, you're not lucky today, try again")
        
print("correct guess is " + str(x))
