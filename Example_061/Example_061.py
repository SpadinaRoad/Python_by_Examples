#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_061
# $ python3 Example_061.py
# $ python3 Example_061.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

061
Draw a triangle.

"""

import turtle

print(__doc__)

# 360 / 3 = 120 degrees
turtle.shape('turtle')
for i in range(0, 3) :
    turtle.forward(200)
    turtle.right(120)
turtle.exitonclick()
