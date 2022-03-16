def dict_to_list(D):
  L=[]
  for key in D:
    L.apppend((key,D[key]))
  return L

def list_to_dict(L):
  D=dict()
  for key,value in L:
    D[key]=value
  return D  