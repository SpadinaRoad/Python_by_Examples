#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_053
# $ python3 Example_053.py
# $ python3 Example_053.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

053
Display a
random
fruit from
a list of
five fruits.

"""

import random

print(__doc__)

list_of_fruits = ['apple', 'peaches', 'pear', 'plum', 'strawberry']
rand_fruit = random.choice(list_of_fruits)
print(f'A random fruit: {rand_fruit}')

