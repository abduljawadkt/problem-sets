 = [ ] 
op = input().split(',') 
whileop[0] != 'END': 
 ifop[0] == 'JOIN': 
 Q.append(op[1]) 
 elif op[0] == 'LEAVE': 
 Q.pop(0) 
 elif op[0] == 'MOVE': 
 member = op[1] 
 Q.remove(member) 
 ifop[2] == 'TAIL': 
 Q.insert(len(Q), member) 
 else: 
 Q.insert(0, member) 
 ifop[0] == 'PRINT': 
 print(','.join(Q)) 
 op = input().split(',')