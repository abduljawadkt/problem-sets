num = input().split(',') 
#accepting comma seperated integers
max = -1
#taking minimum value
for i in range(len(num)): 
 if(int(num[i])>max): 
  max = int(num[i]) 
print(max)