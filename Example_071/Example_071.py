#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_071
# $ python3 Example_071.py
# $ python3 Example_071.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

071
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.

"""

print(__doc__)

sports = ['curling', 'football']
print(f'Here is the list: {sports}')
fav = input('What is your favourite sport? ')
print()
sports.append(fav)
sports.sort()
print(f'Here is the list: {sports}')

