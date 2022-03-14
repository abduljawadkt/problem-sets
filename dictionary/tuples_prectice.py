import string

s=string.ascii_letters

alpha=tuple(list(s))

print(alpha)

sample='abduljawadktwithn()!#@_!)*(_livesinneerolpalam'
print(list(sample))

k=[]
for p in sample:
  if p in alpha:
    k.append(p)

print(k)
l=tuple(k)
print(l)

#if there is no need of change in a list,then convert it to a tuple