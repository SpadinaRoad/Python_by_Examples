#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_066
# $ python3 Example_066.py
# $ python3 Example_066.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

066
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line.

"""

import turtle
import random 

print(__doc__)

turtle.shape('turtle')

colours = ['yellow', 'orange', 'red', 'purple', 'blue', 'green', 'brown', 'black', 'white']
print(f'The starting colours are : {colours}.')

# 360 / 8 = 45 degrees

# Starting point
turtle.penup()
turtle.forward(-300)
turtle.left(90)
turtle.forward(150)
turtle.right(45)
turtle.pendown()

# Draw the octogon
for i in range(8) :
    colour_choice = random.choice(colours)
    print(f'The colour used : {colour_choice}.')
    colours.remove(colour_choice)
    turtle.color(colour_choice)
    turtle.forward(200)
    turtle.right(45)
    
print(f'The colours left: {colours}')
turtle.exitonclick()
