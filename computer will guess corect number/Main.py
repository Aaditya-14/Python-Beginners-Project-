import random

def guess(x):
    low = 1
    high = x
    feedback = ""
    attempted=0
    
    while feedback != "correct":
        if high != low:
            guess_num = random.randint(low, high)
        else:
            guess_num = low
            print(f"The correct number is {guess_num}")
            break
        
        feedback = input(f"The guess number is {guess_num}, say 'high' if the number is high, 'low' if the number is low, and 'correct' if the number is correct: ").lower()
        attempted=attempted+1
        
        if feedback == "high":
            high = guess_num - 1
        elif feedback == "low":
            low = guess_num + 1
        else:
            print(f"The correct number is {guess_num} and the computer guessed it correctly in {attempted} attemped")

guess(100)