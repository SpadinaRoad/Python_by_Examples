#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_006
# $ python3 Example_006.py
# $ python3 Example_006.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

006
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a user-
friendly format.

"""

print(__doc__)
num_bot = input('How many slices of pizza did you buy : ')
num_ate = input('How many slices of pizza did you eat : ')
num_left = int(num_bot) - int(num_ate)
print('')
print(f'You bought {num_bot} slices of pizza.')
print(f'You ate {num_ate} slices of pizza.')
print(f'You have {num_left} slices of pizza left. Enjoy!')
