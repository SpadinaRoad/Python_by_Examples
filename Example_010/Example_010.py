#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_010
# $ python3 Example_010.py
# $ python3 Example_010.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

010
There are 2,204 pounds in a kilogram. Ask the
user to enter a weight in kilograms and convert it
to pounds.

"""

print(__doc__)
weight_kg = float(input('What is your weigth in Kg: '))
weight_lbs = weight_kg * 2.204
print('')
print(f'Your weight is {weight_kg:.1f} kilograms.')
print(f'Your weight is {weight_lbs:.1f} pounds.')
