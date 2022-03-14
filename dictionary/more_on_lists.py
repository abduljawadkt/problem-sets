#we are going to practise something about lists that we learned from lectures

#print geneartor
l1=[1,2,3,4]
l2=[1,3,2,4]

print(l1>l2)
print(l2>l1)

#methods to copy l1 and make new list in 3 formats
l3=l1.copy()
l4=l1[:]
l5=list(l1)

print(l3)
print(l4)
print(l5)

#method to insert
l1.append(5)
print(l1)
l1.insert(6,7)
print(l1)

#methods to remove an element
l1.remove(2)
print(l1)

l1.pop(0)
print(l1)
#that is the difference between pop and remove