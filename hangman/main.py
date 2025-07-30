import random
from hangman_visual import lives_visual_dict
import string

words = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding"]

def random_words(words):
    word = random.choice(words)
    while word == " " or word == "-":
        word = random.choice(words)
    return word.upper()

def hangman():
    word = random_words(words)
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    life = 7

    while len(letters) > 0 and life > 0:
        print("\n" + "=" * 20)
        print(f"Lives left: {life}")
        print(f"Used letters: {' '.join(sorted(used_letters))}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[life])
        print("Word: " + ' '.join(word_list))

        user_letter = input("Enter a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
            else:
                life -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character.")

    if life == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

hangman()
