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


#adding computer guess
def computer_guess(x):
  low=1
  high=x
  feedback=''
  
  while feedback != 'c':
    if low!=high:
    guess=random.randint(low,high)
    else:
      guess=low
      feeback=input(f"is {guess} is a too high,too low or correct?")
    if feedback=='h':
      high=guess-1
    elif feedback=='l':
      low=guess+1
  print(f"yay,you predicted correctly,its {guess}")   
                  
computer_guess(100)  
