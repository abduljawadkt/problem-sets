#hangman is a game whether one to guess the word which is the other \the other one thought by guessing the letters in the word
import random
from words import words

#we need to gat a valid word by removing which does'nt include spaces of '-',so lets def

def get_valid_word(words):
  word=random.choice(words)
  while '' in word or '-' in word:
    word=random.choice(words)
  return words  