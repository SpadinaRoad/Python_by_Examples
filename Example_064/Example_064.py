#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_064
# $ python3 Example_064.py
# $ python3 Example_064.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

064
Draw a five-pointed
star.

"""

import turtle

print(__doc__)

# What is a five-point star from angles
# 360 / 5 = 72 degree angles
# 72 * 2 = 144
# Not keen on thinking about a star

turtle.shape('turtle')

for i in range(0, 5) :
    turtle.forward(100)
    turtle.right(144)
    
turtle.exitonclick()
