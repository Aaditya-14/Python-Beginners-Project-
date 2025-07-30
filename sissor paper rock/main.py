import random
result = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

def win(player, opponent):
        if(player=="s"and opponent=="p")or(player=="r"and opponent=="s")or (player=="p"and opponent=="r"):
            return True


def game():
    user=(input("Enter s for sissor, p for paper and r for rock :").lower())
    com=random.choice(["s","r","p"])
    
    print(f"You chose {result[user]} and computer chose {result[com]}")
    
    if user==com:
        print("its a tie")
    elif win(user,com):
        print("player win")
    else:
        print("computer win")
        


game()
        
