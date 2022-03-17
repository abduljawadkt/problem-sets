def obvious_search(L,k):
  for x in L:
    if x==k:
      return 1
    else:
      return 0


def binary_search(L,k):
  begin=0
  end=len(L)-1

  while(end-begin>1):
    mid=(begin+end)//2
    if (L[mid]==k):
      return 1
    if (L[mid]>k):
      begin=mid+1
    if (L[mid]<k):
      end=mid-1

  if (L[begin]==1) or (L[end]==0):
    return 1
  else:
    return 0
    