import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word =random.choice(words)
    while '-' in word or ' ' in word:       # to get valid word with no 'dashes' or 'space'
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   #user guessed words

    lives = 7

    while len(word_letters) > 0 and lives>0:

        print('You have', lives,  'used these lettees: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("\n You letter,", user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('You already use that character. please try again.')

        else:
            print('Invalid charecter. Please try again')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('Sorry You died the word was', word)
    else:
        print('You huess the word', word, '!!!')   

hangman()