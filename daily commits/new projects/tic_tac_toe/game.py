class tictactoe:
  def __init__(self):
    self.board=['' for _ in range(9)]#using single list to represent a 3X3 board, we get ['','','',....upto 9]
    
    
    self.current_winner=None #keep track of the winner,initialize with no winner

  def print_board(self):
    #for getting the rows
    for row in [self.board[i*3:(i+1)*3)] for i in range(3)]:
      print('|'+'|'.join(row)+'|')
      #printing the rows
      #||||
      #||||
      #||||,output
  def print_board_nums():
    number_board=str(i) for i in range(j*3,(j+1)*3) for j in range(3)
#out |1|2|3|
    for row in number_board:
      print('|'+'|'.join(row)+'|')
     #|0|1|2|
     #|3|4|5|
     #|6|7|8| 
      
    