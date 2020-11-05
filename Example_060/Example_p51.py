#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_060
# $ python3 Example_p51.py
# $ python3 Example_p51.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

Page 51 example

"""

import turtle

print(__doc__)

print('Menu')
print('A. Triangle')
print('B. Square')
print('C. Pentagon')
print('D. Hexagon')
print('E. Circle')
print('F. Nested')

print()

choice = input('Enter choice: ')
choice = choice.lower()

turtle.shape('turtle')

if choice == 'a' : 
    # 360 / 3 = 120
    for i in range(0, 3) :
        turtle.forward(200)
        turtle.right(120)
    turtle.exitonclick()
    
elif choice == 'b' : 
    # 360 / 4 = 90
    for i in range(0, 4) :
        turtle.forward(200)
        turtle.right(90)
    turtle.exitonclick()
    
elif choice == 'c' : 
    # 360 / 5 = 72
    for i in range(0, 5) :
        turtle.forward(100)
        turtle.right(72)
    turtle.exitonclick()

elif choice == 'd' :
    # 360 / 6 = 60
    for i in range(0, 6) :
        turtle.forward(200)
        turtle.right(60)
    turtle.exitonclick()

elif choice == 'e' :
    # 360 / 36 = 10
    for i in range(0, 36) :
        turtle.forward(20)
        turtle.right(10)
    turtle.exitonclick()

elif choice == 'f' :
    for i in range(0, 10) :
        turtle.right(36)
        for j in range(0, 5) :
            turtle.forward(100)
            turtle.right(72)
    turtle.exitonclick()
    
