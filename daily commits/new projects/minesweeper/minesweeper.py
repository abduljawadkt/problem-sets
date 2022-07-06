#1.we need to print a table of a size.(eg:10)
#2.we need to randomly add bombs
#3.user dig anywhere
#4.if bomb is there,show game over
#5.if no bomb present there,dig next box

class Board:
  def __init__(self,dim_size,num_bombs):
    #parameters needed to make table
    self.dim_size=dim_size
    self.num_bombs=num_bombs
    #we need to create the board

    self.board=self.make_new_board
    #helper function is using here

    self.dug=set()
    #if we dug ar 0,0 ,it returns as {0,0}
    #to construct a new board based on dimension size and no. of bombs
    #data saved as tuple to represent the board

def play(dim_size=10,num_bombs=10):
  #game algorithm
  pass