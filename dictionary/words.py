class Word: 
 count = 0
 def __init__(self, word, pos): 
 Word.count += 1
 self.word = word 
 self.pos = pos 
 def print_info(self): 
 print(f'The word is "{self.word}" and its part of speech is "{self.pos}".') 
inp_1 = input() 
inp_2 = input() 
word = Word(inp_1, inp_2) 
word.print_info() 