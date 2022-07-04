#we need to write code for binary search here
#we have to show that binary search is faster than naive search
#algorithm for naive search
#algorithm for binary search

def naive_search(l,target):
  #l is the list and taget is the element to be find
  for i in range(len(l)):
    if l[i]==target:
      return i
  return -1
#basic code for naive search
#l=[1,2,3,4,5,6,7]
#naive_search(l,5)


#lets move to binary search
#binary search is a midpoint based searching mechanism
def binary_search(l,target):
  midpoint=len(l)//2

  #if midpoint,we return midpoin itself
  if l[midpoint]==target:
    return midpoint

  elif target<l[midpoint]:
    return binary_search(l,target)
  else:
    return binary_search(l,target)
  #code structure  