import random



while True:
    User_input=input("Enter (Y/N): ").upper()
    if User_input=="Y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"Dice Rolled and the no in dice is {dice1},{dice2}")
    elif User_input=="N":
        print("See You Next Time")
        break
    else:
        print("Invalid character please enter valid character")
        break