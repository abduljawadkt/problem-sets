import random
#import math

#object
#thigs to do for a player
class player:
  def __init__(self,letter):
    #it is x or o
    self.letter=letter
  #we want to define the move of a player
  def get_move(self,game):
    pass
#placeholder.

class computerplayer(player):
  #method of inheritance is used by taking class player as a parent class
  def __init__(self,letter):
    super().__init__(letter)
    #superclass is used here.#temporary

  def get_move(self,game):
    square=random.choice(game.availble_moves())
    
class humanplayer(player):
  #inheritance

  def __init__(self,letter):
    super().__init__(letter)

  def get_move(self,game):
    #here we want to iterate untill we find a valid square
    valid_square=False
    val=None
    while not valid_square:
      square=input(self.letter+'\'s turn.input move(0-9):')
      try:
        val=int(square)
        if val not in game.available_moves():
          #chech whether the move could be done
          raise ValueError
          
        valid_square=True
        #if the above code become successful
        #try-except
        #error handling
      except ValueError:
        print('Invalid Square,Try again')
    return val

    def geniuscomputerplayer(player):
      def __init__(self,letter):
          super().__init__(letter)
      def get_move(self,game):
        if len(game.available_moves()) == 9:
          square = random.choice(game.available_moves())
        else:
          square = self.minimax(game, self.letter)
      return square

      def minimax(self,state,player):
        max_player=self.letter



