from player import humanplayer ,computerplayer
import math
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
      #it can also helpful to make empty boards
  def print_board_nums():
    number_board=str(i) for i in range(j*3,(j+1)*3) for j in range(3)
#out |1|2|3|
    for row in number_board:
      print('|'+'|'.join(row)+'|')
     #|0|1|2|
     #|3|4|5|
     #|6|7|8| 

  def availble_moves(self):
    return [i for i,spot in enumerate(self.board) if spot=='']
    
      #enumerate converts to (index,element) format as tuple
      #gives index number of empty areas
  
    #it returns the index numbers of empty spaces
  def empty_squares(self):
    return '' in self.board

  def num_empty_squares(self):
    return self.board.count('')
    #return number of empty squares

  def make_move(self,square,letter):
    #if valid move,it will assign square to letter
    if self.board[square]=='':
      #to represent availble square in board
      self.board[square]=letter
      if self.winner(square,letter):
        self.current_winner=letter
        
      return True
    return False  

  def winner(self,square,letter):
    #for that we need to check the row
    row_ind=square//3
    #we get row index while doing stage division
    row=self.board[row_ind*3:(row_ind+1)*3]
    #the above formula return the index of row
    #roundoff method is using here


    
    if all([spot==letter for spot in  row]):
      #if all means that if everything in the list is true
      return True
    
    #we need to check_coloumn also
    col_ind=square % 3
    #reminder method is using here
    #above formula returns the column number
    column=[self.board[col_ind+i*3] for i in range(3)]
    if all(spot==letter for spot in column]):
      return True
    
    #next we want to check_diagonals
      #digonals only have index numbers 0,2,4,6,8
      #lets make a formula for it
    if square%2==0:
       diagonal1=[self.board[i] for i in [0,4,8]]
       if all(spot==letter for spot in diagonal1):
         return True
       diagonal2=[self.board[i] for i in [2,4,6]]
       if all(spot==letter for spot in diagonal2):
         return True
    #if all these checks fails
    return False     
    


def play(game,x_player,o_player,print_game=True):
  if print_game:
    game.print_board_nums()
      #return number board with index nums.(above given)
  letter = 'X'
  while game.empty_squares():
    if letter=='O':
      square=o_player.get_move(game)
    else:
      square=x_player.get_move(game)
      
    if game.make_move(square,letter):
      if print_game():
        print(letter + f'make move to {square}')
        game.print_board()
        print('')
        #just empty line  

      if game.current_winner:
        if print_game:
          print(letter+'wins!')
        return letter  
          
      letter='O' if letter =='X' else 'X'
        #this is equalent to if else statement

  if print_game:
    print('it\s a tie!')

if __name__=='__main__':
  x_player=humanplayer('X')
  o_player=computerplayer('O')
  t=tictactoe()
  play(t,x_player,o_player,print_game=True)
  
