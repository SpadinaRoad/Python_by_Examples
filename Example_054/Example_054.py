#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_054
# $ python3 Example_054.py
# $ python3 Example_054.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

054
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.

"""

import random

print(__doc__)

your_choice = ''
comp_wins = 0
my_wins = 0 
h_t_dict = { 'h' : 'heads', 't' : 'tails'}
while your_choice != 'x' :
    heads_or_tails = random.choice(['h', 't'])
    your_choice = input('Choose heads or tails (h/t) : ')
    your_choice = your_choice.lower()
    if your_choice != 'x' :
        print()
        if heads_or_tails == your_choice :
            print('You win.')
            my_wins += 1
        else : 
            print('Bad luck')
            comp_wins += 1
        print(f'You chose          : {h_t_dict[your_choice]}')
        print(f'The computer chose : {h_t_dict[heads_or_tails]}')
        print(f'The score: Computer {comp_wins} Me {my_wins}')
    print()
    
