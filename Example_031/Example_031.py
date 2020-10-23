#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_031
# $ python3 Example_031.py
# $ python3 Example_031.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

031
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius 2 ).

"""

print(__doc__)

from math import pi

num = ''
while num != 'x' : 
    num = input('Enter the radius of a circle : ')
    if num != 'x' : 
        num = float(num)
        area = pi * num * num
        print(f'The input for a radius : {num}.')
        print(f'The area of the circle is : {area}.')

        
