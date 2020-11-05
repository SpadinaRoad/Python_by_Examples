#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_068
# $ python3 Example_068.py
# $ python3 Example_068.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

068
Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn.

"""

import turtle
import random 

print(__doc__)

turtle.shape('turtle')

# Create random variables of a shape
shape_lines = random.randint(3, 10)
line_length = random.randint(0, 200)
line_angle  = 360 / shape_lines
#num_shapes = int(360 / line_angle * 4)

shapes  = {3: 'triangle', 4 : 'square', 5 : 'penatagon', 6 : 'hexagon', 8 : 'octagon'}
print(f'The shape : {shape_lines} lines or {shapes.get(shape_lines)}')
print(f'The length of each line : {line_length}')
print(f'The shape angle : {line_angle:.3f}')

turtle.penup()
turtle.left(90)
turtle.forward(line_length)
turtle.pendown()
turtle.right(180)

# Draw a shape
for i in range(shape_lines) : 
    turtle.forward(line_length)
    turtle.right(line_angle)

turtle.exitonclick()
