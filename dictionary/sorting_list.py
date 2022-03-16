def mini(L):
  mini=L[0]
  for x in L:
    if x<mini:
      mini=x
  return mini

def sort(L):

  m=mini(L)
  L.remove(m)
  return [m]+sort(L)
