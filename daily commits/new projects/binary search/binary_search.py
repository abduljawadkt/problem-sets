import random


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
def binary_search(l,target,low=None,high=None):
  if low is None:
    low=0
  
  if high is None:
    high=len(l)-1

  if high<low:
    return -1

  
  midpoint=(low+high)//2
  #we could deal with any kind of alterations in the list

  #if midpoint,we return midpoin itself
  if l[midpoint]==target:
    return midpoint

  elif target<l[midpoint]:
    return binary_search(l,target,low,midpoint-1)
  else:
    return binary_search(l,target,midpoint+1,high)


if __name__=='__main__':
  
#  l=[1,2,3,4,5,6,7,8,9,12]
# target=10
#  print(naive_search(l,target))
# print(binary_search(l,target))

#lets do another snippet of code to search a word from a random list
  length=1000
  sorted_list=set()
  while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length,3*length))
  sorted_list=sorted(sorted_list)  
  
    