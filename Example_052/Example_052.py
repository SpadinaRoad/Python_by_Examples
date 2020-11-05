#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_052
# $ python3 Example_052.py
# $ python3 Example_052.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

052
Display a
random
integer
between
1 and 100
inclusive.

"""

import random

print(__doc__)

rand_num = random.randint(1, 100)
print(f'A random number: {rand_num}')

