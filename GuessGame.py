# This is a guess the number game. 
import random
guessesTaken = 0  
print('Hello! What is your name?') 
myName = input()   
number = random.randint(1, 20) 
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') 

def repeat():
    correct_value = False
    while not correct_value:
        try:
            guess = int(input())
        except ValueError:
            print("Please Enter a Number")
        else:
            correct_value = True
    return guess


while guessesTaken < 6: 
    print('Take a guess.')
    guess = repeat()
        
    guessesTaken = guessesTaken + 1 
 
    if guess < number: 
     print('Your guess is too low.') # There are eight spaces in front of print. 
    if guess > number: 
        print('Your guess is too high.') 
    if guess == number: 
        break 
if guess == number: 
     guessesTaken = str(guessesTaken) 
     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') 
if guess != number: 
     number = str(number) 
     print('Nope. The number I was thinking of was ' + number) 