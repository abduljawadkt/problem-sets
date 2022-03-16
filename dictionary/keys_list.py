'''
function to print list of keys for a specific value
'''
def value_to_keys(D,value):
  for key in D:
    values=[]
    if D[key]==value:
      values.append(D[key])
  return values  
    