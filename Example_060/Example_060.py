#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_060
# $ python3 Example_060.py
# $ python3 Example_060.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

060
Draw a square.

"""

import turtle

print(__doc__)

# 360 / 4 = 90 degrees
turtle.shape('turtle')
for i in range(0, 4) :
    turtle.forward(200)
    turtle.right(90)
turtle.exitonclick()
