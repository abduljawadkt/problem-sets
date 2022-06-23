#hangman is a game whether one to guess the word which is the other \the other one thought by guessing the letters in the word
import random
from words import words

#we need to gat a valid word by removing which does'nt include spaces of '-',so lets def

def get_valid_word(words):
  word=random.choice(words)
  while '' in word or '-' in word:
    word=random.choice(words)
  return words  

#hangman
def hangman():
    word=get_valid_word(words)
    word_letter=set(word) #letters of the word
    alphabet=set(string.ascii_uppercase) #letter of the english dictionary
    used_letters=set()  #what the letters user has guessed
    
    #user input
    user_letter=input("Enter a letter: ")
    if user_letter in alphabet-used_letters:
        used_letters.add(user_letter)
        is user_letter in word_letter:
            word_letter.remove(user_letter)
  