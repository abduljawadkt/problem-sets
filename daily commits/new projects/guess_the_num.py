#random
#random range
#guess function 
#while loop 
#guess equals
#if else statement

#library
import random

def guess(x):
  random_number=random.randint(1,x)
  guess=0
  while guess!=random_number:
    guess=int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_number:
      print("sorry,Guess again.Too low")
    elif guess > random_number:
      print("sorry,guess again.too high")
  print(f"congrats,you picked the correct number{random_number}correctly")         