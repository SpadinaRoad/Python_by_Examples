#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_070
# $ python3 Example_070.py
# $ python3 Example_070.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

070
Add to program 069 to ask the
user to enter a number and
display the country in that
position.

"""

print(__doc__)

countries = ('Canada', 'Scotland', 'Sweden', 'Greece', 'France')
print(f'The countries are: {countries}')

guess = int(input('Enter a number (0 to 4) : '))
print(f'The country at index {guess} is {countries[guess]}')

