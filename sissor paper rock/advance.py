from ursina import *
import random

app = Ursina()

choices = ['rock', 'paper', 'scissors']
short_map = {'rock': 'r', 'paper': 'p', 'scissors': 's'}

def win(player, opponent):
    return (player == 's' and opponent == 'p') or \
           (player == 'r' and opponent == 's') or \
           (player == 'p' and opponent == 'r')

result_text = Text('', origin=(0, 0), scale=2, y=0.3)

def play(player_choice):
    player = short_map[player_choice]
    opponent = random.choice(['r', 'p', 's'])
    
    player_full = player_choice
    opponent_full = [k for k, v in short_map.items() if v == opponent][0]

    if player == opponent:
        result = f"Both chose {player_full}. It's a tie!"
    elif win(player, opponent):
        result = f"You chose {player_full}, Computer chose {opponent_full}. You win!"
    else:
        result = f"You chose {player_full}, Computer chose {opponent_full}. You lose!"
    
    result_text.text = result

# UI buttons
rock_btn = Button(text='Rock', color=color.azure, scale=0.2, position=(-0.5, -0.3))
paper_btn = Button(text='Paper', color=color.orange, scale=0.2, position=(0, -0.3))
scissors_btn = Button(text='Scissors', color=color.red, scale=0.2, position=(0.5, -0.3))

rock_btn.on_click = lambda: play('rock')
paper_btn.on_click = lambda: play('paper')
scissors_btn.on_click = lambda: play('scissors')

app.run()
