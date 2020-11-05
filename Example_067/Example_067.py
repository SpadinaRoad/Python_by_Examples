#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_067
# $ python3 Example_067.py
# $ python3 Example_067.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

067
Create the following pattern:

(The pattern is an overlay of octogons to create a circle.)

"""

import turtle
import random 

print(__doc__)

turtle.shape('turtle')

shapes  = {3: 'triangle', 4 : 'square', 5 : 'penatagon', 6 : 'hexagon', 8 : 'octagon'}

# Shape Sides
shape_sides = 8

# Angles in a shape
shape_angle = 360 / shape_sides

# Number of shapes in a cirle
num_shapes = 10

# Angles for shape
angle = 360 / num_shapes

distance = 200 * (1 / shape_sides) * 3

print('Creating an image : ')
print(f'The internal image is {shape_sides} sided. AKA: {shapes.get(shape_sides)}')
print(f'The internal angles are : {shape_angle}.')
print(f'We will write: {num_shapes} {shape_sides}-sided shapes in a circle.')

for j in range(num_shapes) : 
    # Create an octagon
    for i in range(shape_sides) : 
        turtle.forward(distance)
        turtle.right(shape_angle)
    turtle.right(angle)

turtle.exitonclick()
