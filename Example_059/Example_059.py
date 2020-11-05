#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_059
# $ python3 Example_059.py
# $ python3 Example_059.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

059
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.

"""

import random

print(__doc__)

colours = ['yellow', 'orange', 'red', 'purple', 'blue', 'green']
rand_colour = random.choice(colours)
your_colour = ''

while your_colour != rand_colour :
    print(f'List of colours to choose from: {colours}')
    your_colour = input('Pick a colour: ')
    your_colour = your_colour.lower()
    print(f'The input for the colour choice: {your_colour}')
    
    if your_colour == rand_colour :
        print('Well done.')
    else :
        if rand_colour == 'yellow' :
            print('The sun is brightly YELLOW.')
        elif rand_colour == 'orange' :
            print('The sun is now a mellow ORANGE.')
        elif rand_colour == 'red' :
            print('I am hot to trot.')
        elif rand_colour == 'purple' :
            print('I am feeling royal.')
        elif rand_colour == 'blue' :
            print('You are probably feeling BLUE right now')
        elif rand_colour == 'green' :
            print('I bet you are GREEN with envy')
    print()
