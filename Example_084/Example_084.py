#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_084
# $ python3 Example_084.py
# $ python3 Example_084.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

084
Ask the user to type in their
postcode. Display the first
two letters in uppercase.

I don't know UK postcodes, using Canadian version: A1B 2C3
"""

print(__doc__)

postal_code = input('Enter your postal code : ')
print(f'The input for a postal code: {postal_code}')
print()
print(f'Postal Code: {postal_code.upper()}')
print()
