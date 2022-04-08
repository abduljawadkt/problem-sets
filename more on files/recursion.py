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
