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
        