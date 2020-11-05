#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_085
# $ python3 Example_085.py
# $ python3 Example_085.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

085
Ask the user to type in their name
and then tell them how many vowels
are in their name.

"""

print(__doc__)

fname = input('Enter your name: ')
print(f'The input for a name: {fname}')
vowels_ct = 0
for i in fname : 
    if i in 'aeiouAEIOU' :
        vowels_ct += 1

print(f'There are {vowels_ct} vowels in your name.')

