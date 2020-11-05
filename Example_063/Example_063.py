#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_063
# $ python3 Example_063.py
# $ python3 Example_063.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

063
Draw three squares
in a row with a gap
between each. Fill
them using three
different colours.

"""

import turtle
import random

print(__doc__)

num = 0
while num <= 0 or num >= 9 : 
    num = int(input('How many squares to draw? : '))

colours = ['blue', 'red', 'yellow', 'orange', 'black', 'brown', 'green', 'purple' ]
colours_used = []

turtle.shape('turtle')
turtle.penup()
turtle.forward(-400)
turtle.pendown()

for j in range(0, num) :
    turtle.begin_fill()
    colour_choice = random.choice(colours)
    colours_used.append(colour_choice)
    colours.remove(colour_choice)
    turtle.color(colour_choice)

    for i in range(0, 4) :
        turtle.forward(100)
        turtle.left(90)        

    turtle.end_fill()
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
    
turtle.exitonclick()

print(f'The colours used : {colours_used}.')
print(f'The colours left : {colours}')
