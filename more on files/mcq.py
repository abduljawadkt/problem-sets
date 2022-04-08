class MCQ(Question): 
 def __init__(self, statement, marks, ops, c_ops): 
 super().__init__(statement, marks) 
 self.ops = ops # list of all options 
 self.c_ops = c_ops # list of correct options 
 def print_question(self): 
 super().print_question() 
 for i in range(4): 
 print(self.ops[i]) 