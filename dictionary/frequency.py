freq=dict()
L=input().split(',')

for word in L:
  freq[word]=0

for word in L:
  freq[word]=freq[word]+1
  