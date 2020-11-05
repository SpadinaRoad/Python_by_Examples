#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_069
# $ python3 Example_069.py
# $ python3 Example_069.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

069
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.

"""

print(__doc__)

countries = ('Canada', 'Scotland', 'Sweden', 'Greece', 'France')
print(f'The countries are: {countries}')

guess = input('Pick a country : ')
print(f'The country {guess} is at index : {countries.index(guess)}')

