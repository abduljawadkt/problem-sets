def check0(L):
  if (len(L)==0):
    #gives false if the list is empty 
    return 0
  if (L[0]==0):
    return 1
    #gives true that is 1 if the syntax works.which is searching for zero
  else:
    return check0(L[1:len(L)])
#proper recursion occurs here
L=[1,2,3,4,5,5,6,7,0,9]
ans=check0(L)
print(ans)
