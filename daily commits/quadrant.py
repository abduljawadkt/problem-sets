x = float(input("Enter the x-axis:")) 
y = float(input("Enter the y-axis:")) 
#inputs the x and y axis


if x>0: 
 if y>0: 
  print("first") 
elif y<0: 
 print("fourth") 
elif(y==0): 
 print("x-axis") 
if x<0: 
 if y>0: 
  print("second") 
elif(y<0): 
 print("third") 
elif(y==0): 
 print("x-axis") 
if x==0: 
 if y==0: 
  print("origin") 
 else: 
  print("y-axis")
#the above snippet of code is to print quadrants according to the axes input
