import random
import string
from words import word

hangman_word = random.choice(word).upper()
#print(hangman_word)

def hangman():
    word_letters = set(hangman_word) # letters in the word
    alphabet = set(string.ascii_uppercase) # initialized upper case letters
    used_letters = set() #what the user has guessed

    while len(word_letters) > 0:
    #getting user input
        print("Word is: ", hangman_word)
        print("You have used these letters: ", " ".join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else "-" for letter in hangman_word]

        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        print("\n")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try again\n")

        else:
            print("Invalid character\n")

    print("You have guessed the word!!! now gtfo")

hangman()