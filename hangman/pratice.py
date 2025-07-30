import random
import string


words = ["aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding"]


def random_word(words):
    word=random.choice(words)
    while word == " " or word=="-":
        word=random.choice(words)
    return word.upper()

def hangman():
    word=random_word(words)
    letter=set(word)
    alpa=set(string.ascii_uppercase)
    used_letter=set()
    
    while len(letter)>0:
        
        
        user_letter=input("Enter any letter")
        if user_letter==alpa-used_letter:
            used_letter.add(used_letter)
            if user_letter in letter:
                used_letter.remove(user_letter)
        elif user_letter in used_letter:
            print("u already use this")
        else:print("Invalid character=")
            
    


hangman()
