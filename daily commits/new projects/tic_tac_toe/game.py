class tictactoe:
  def __init__(self):
    self.board=['' for _ in range(9)]#using single list to represent a 3X3 board
    self.current_winner=None #keep track of the winner,initialize with no winner

  def print_board(self):
    #for getting the rows
    for row in [self.board[i*3:(i+1)*3)] for i in range(3)]:
      print('|'+'|'.join(row)+'|')
      #printing the rows
  