import random
#to use mathematical functions
import math
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
    pass
    
class humanplayer(player):
  #inheritance
  def __init__(self,letter):
    super().__init__(letter)

  def get_move(self,game):
    pass
    