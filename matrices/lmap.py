def lmap(letter): 
 letter_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
 return letter_map.index(letter) + 1
label = input() 
n = len(label) 
def colnum(label): 
 n = len(label) 
 val = lmap(label[0]) 
 if n == 1: 
 return val 
 return val * 26 ** (n - 1) + colnum(label[1: ]) 
print(colnum(label))