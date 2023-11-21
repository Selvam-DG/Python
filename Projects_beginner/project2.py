# Guess the number
# Random number is used t built this program

import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while(random_number != guess_number):
        guess_number = int(input("Enter the numberb between 1 and {}: ".format(x)))
        if guess_number < random_number:
            print("Sorry! guess again. Number is too low")
        elif guess_number > random_number:
            print("Sorry! guess again. Number is too high")
        else:
            pass
        
    print("Congrats! You have correctly Guessed the  number")
        

def computer_guess(x):
    low = 1
    high  = x
    feedback = ''
    
    while feedback !='c':
        if low != high:
            guess_number = random.randint(low,high)
            
        else:
            guess_number = low
        feedback = input(f"IS {guess_number} too High(H) or too Low(L) or Correct(C): ").lower()
        if feedback == 'h':
            high = guess_number-1
        elif feedback == 'l':
            low = guess_number+1
    print(f"Ohhh!!!! The computer guess the number {guess_number} correctly")            
        
computer_guess(100)      
        
        
        
        
        
        