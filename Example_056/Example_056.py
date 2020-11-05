#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_056
# $ python3 Example_056.py
# $ python3 Example_056.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

056
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.

"""

import random

print(__doc__)

rand_num = random.randint(1, 10)
guess = ''

while guess != rand_num and guess != 'x' :

    guess = input('Enter a number : ')
    if guess != 'x' :
        guess = int(guess)
        if guess != rand_num :
            print(f'Your choice, {guess}, is not a match.')
        else :
            print(f'Your choice matches: {guess}')
    print()
            
            
