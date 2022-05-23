s=input().lower() 
#accept word in lower case
a='abcdefghijklmnopqrstuvwxyz' 
t='' 
for x in a: 
 for y in s: 
   if x==y:
     #checking if same letter inside the word
     t+=y 
print(t) 