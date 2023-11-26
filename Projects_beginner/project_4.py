import random

# rock  beats scissors or scissors beat paper and paper beats rocks

def play():
    user = input(" 'r' for rock, 'p' for paper,'s' for scissor \n what's your choice?  ")
    computer_choice = random.choice(['r','p','s'])
    
    
    if user == computer_choice:
        return 'It\s a Tie'
    
    if is_win(user,computer_choice):
        return 'You Won'
    
    # if is_win (computer_choice,user):
    #     return "You lost"
    
    return 'You lost'


def is_win(player, opponent):
    # r>s, s>p ,p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')or (player == 'p' and opponent == 'r'):
        
        return True
    
print(play())