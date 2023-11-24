import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly choose value from the list
    
    while('-'in word or ' ' in word):
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    
    word_letter = set(word.upper())  # letters in word
    
    alphabet = set(string.ascii_uppercase)
    used_letter = set()   # what the user has guessed
    # print(word)
    # print(word_letter)
    # print(len(word_letter))
    # print(alphabet)
    # x = input("Enter a letter:").upper()
    # if x in word_letter:
    #     print('Yes')
    # else:
    #     print('No')
    
    lives = 6
    
    while len(word_letter) >0 and lives>0:
        
        
        print('You have', lives, 'lives left and you have used these letter: ',' '.join(used_letter))
        
        # # what the current word is 
        word_list = [letter if letter in used_letter else '-' for letter in word.upper() ]
        
        print('Current word : ' ,' '.join(word_list))
        
        # # getting user input
        
        user_letter = input("Guess a letter : ").upper()
        
        if user_letter in (alphabet - used_letter):
            used_letter.add(user_letter)
            
            # user entered the letter which is in the word
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print("Sorry, Letter is not in Word")
                
        
        elif user_letter in used_letter:
            print('You have already used that character. please try again')

        else:
            print("Invalid character. Please try again")

    if lives ==0:
        print('Sorry!!!! You have lost. Better luck next time. The word was ',word.upper())
    else:
        print('You guessed the word', word.upper())
    
hangman()

    
    
    
    
    