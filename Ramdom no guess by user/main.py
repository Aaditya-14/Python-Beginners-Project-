import random

def com(x):
    computer = random.randint(1, x)
    user = int(input(f"Enter any number between 1 and {x}: "))
    i=0
    
    while computer != user:
        print("You guess if wrong")
        i=i+1
        
        if computer > user:
            print("Too low! Try a higher number")
        elif computer < user:
            print("Too high! Try a lower number")

        user = int(input(f"Try again. Enter a number between 1 and {x}: "))
        
    print(f"correct answer you guess it in {i} tries")
    
com(20)
