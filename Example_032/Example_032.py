#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_032
# $ python3 Example_032.py
# $ python3 Example_032.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

032
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.

"""

print(__doc__)

from math import pi

radius = ''
while radius != 'x' : 
    radius = input('Enter the radius of a cyclinder : ')
    if radius != 'x' : 
        radius = float(radius)
        height = input('Enter the height of a cyclinder : ')
        height = float(height)
        volume = pi * radius * radius * height
        print(f'The input for the radius : {radius}.')
        print(f'The input for the height : {height}.')
        print(f'The volume of the cyclinder is : {volume}.')

        
