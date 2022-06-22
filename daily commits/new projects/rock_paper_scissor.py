import random

def play():
  user=input("what is your choice?'r' for rock,'p' for paper,'s' for scissor")
  computer=random.choice(['r','p','s'])
  if user==computer:
    return 'tie'
