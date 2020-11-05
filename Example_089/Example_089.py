#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_089
# $ python3 Example_089.py
# $ python3 Example_089.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

089
Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).

"""

from array import *
import random

print(__doc__)

int_array = array('i', [])

for i in range(5) :
    int_array.append(random.randint(0,500))

for i in int_array : 
    print(i)    
