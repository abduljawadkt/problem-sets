from words import words
import string
import random

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or '' in word:
        word=random.choice(words)
    return words

def hangman():
    word=get_valid_word(words)
    word_letter=set(word) #letters of the word
    alphabet=set(string.ascii_uppercase) #letter of the english dictionary
    used_letters=set()  #what the letters user has guessed
    
    while len(word_letter)>0:
        print("You have used these letters: ",''.join(used_letters))
        #join used to conevrt(['a','b','cd']) to 'a b cd'
        
        word_list=[letter if letter in used_letters else '-' for letter in word]
        #like what current word is W-RD
        print("current word: ",''.join(word_list))
        user_letter=input("Enter a letter: ")
        if user_letter in alphabet-used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letter:
            word_letter.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used this letter,print another letter")
        else:
            print("invalid character,try again")
