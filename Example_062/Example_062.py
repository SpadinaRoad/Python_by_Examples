#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_062
# $ python3 Example_062.py
# $ python3 Example_062.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

062
Draw a circle.

"""

import turtle

print(__doc__)

# 360 / 360 = 1 degrees
turtle.shape('turtle')
for i in range(0, 360) :
    turtle.forward(2)
    turtle.right(1)

# Easier cirlce
turtle.penup()
turtle.right(190)
turtle.forward(300)
turtle.pendown()
for i in range(0, 36) :
    turtle.forward(20)
    turtle.right(10)
turtle.exitonclick()
