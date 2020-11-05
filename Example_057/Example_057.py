#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_057
# $ python3 Example_057.py
# $ python3 Example_057.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

057
Update
program 056
so that it
tells the
user if they
are too high
or too low
before they
pick again.

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
            if guess > rand_num :
                print('Your choice is too high.')
            else :
                print('Your choice is too low.')
        else :
            print(f'Your choice matches: {guess}')
    print()
 
