import math
import random

class Player:
    
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self,game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        print('Please play')
        return square
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            
            square = input(self.letter + '\'s Turn . Input move to (0-8) :')
            
            
            try:
                val  = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
            
            
# p = Player('x')
# c =p.letter
# print(c)

# rcp = RandomComputerPlayer(p)
# a = rcp.letter
# print('  busss ', a)
