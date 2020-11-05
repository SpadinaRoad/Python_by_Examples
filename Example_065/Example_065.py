#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_065
# $ python3 Example_065.py
# $ python3 Example_065.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

065
Write the numbers as shown below,
starting at the bottom of the number
one.

(The imagine shows 1 2 3 written as by hand with straight lines.)

"""

import turtle

print(__doc__)

turtle.shape('turtle')
turtle.penup()

# Draw 1
# a. Move to starting point
turtle.forward(-200)
turtle.left(90)
turtle.forward(200)
turtle.right(180)
# b) Draw the number
turtle.pendown()
turtle.forward(300)
turtle.penup()

# Draw 2
# a. Move to starting point
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(300)
# b) Draw the number
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.penup()

# Draw 3
# a. Move to starting point
turtle.forward(100)
# b) Draw the number
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()
