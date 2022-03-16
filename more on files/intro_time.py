'''
here we calculate the time taken to perform a function
'''

import time


def sea(L,k):
  for x in L:
    if x==k:
      return 1
    else:
      return 0

L=[]
for i in range(100):
  L.append(i)
print(L)  
  


a=time.time();sea(L,3);b=time.time();sea(L,30);print(b-a);c=time.time();sea(L,99);d=time.time();print(d-c)

