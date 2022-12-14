#game_begins

class Board:
  __init__(self, dim_size, num_bombs):
  self.dim_size = dim_size
  self.num_bombs = num_bombs
  #initialised a board class and added attributes towards it

  self.board = self.make_new_board()
  #to plant new bombs

  self.dug = set() #if we dig at 0, 0,then self.dug = {(0,0)}

  def make_new_board(self)
  #construct a new board based on dimension size and num bombs
  #we should construct list of lists
  #but it is a 2D board

  #generating a new board
  Board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

  
def play (dim_size == 10 , num_bombs == 10 ):
  #step 1 : create a new board and plant new bombs
