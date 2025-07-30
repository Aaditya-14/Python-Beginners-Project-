import random

Alphabate="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbol="!@#$%^&*()_"
combine_word=Alphabate+number+symbol

def password (length=12):
    for i in range (length):
        password=random.choice(combine_word)
        print(password , end='')
        
    
password()