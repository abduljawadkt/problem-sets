def obs(L,k):
  for x in L:
    if x==k:
      return k
  return 0    
 
    

def binary_search(L,k):
  #defining begin and the end of the list
  begin=0
  end=L[len(L)-1]

  #next we need to apply the while conditioning for 2 digit list
  while((end-begin)>1):
    #finding middle element
    mid=begin+end//2
    if L[mid==k]:
      return 1

    if k>L[mid]:
      begin=L[mid+1]
      return 1

    if k<L[mid]:
      end=L[mid-1]
      return 1

    if (L[begin]==k) or (L[end]==k):
      return 1
    else:
      return 0
      

L=list(range(1000000)) 


def binary_search(L,100)