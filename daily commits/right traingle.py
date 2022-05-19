x = int(input()) 
y = int(input()) 
z = int(input()) 
# There are three possible conditions 
# We are combining them using the "or" operator 
if ((x ** 2 + y ** 2 == z ** 2) or 
 (y ** 2 + z ** 2 == x ** 2) or 
 (z ** 2 + x ** 2 == y ** 2)): 
 print('YES') 
else: 
 print('NO') 