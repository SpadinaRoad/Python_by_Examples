#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_035
# $ python3 Example_035.py
# $ python3 Example_035.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

035
Display the following message:

1. Square
2. Triangle
Enter a Number: 

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.

"""

print(__doc__)

from math import pi

choice = ''
while choice != 'x' : 
    print('Calculate Area For ')
    print('1. Square')
    print('2. Triangle')
    choice = input('Enter a Number : ')
    
    print(f'The input for the choice : {choice}.')
    print()
    
    if choice != 'x' : 
        if choice == '1' : 
            # Square
            square_len = int(input('What is the length of the square : '))
            print(f'The input for the length : {square_len}.')
            
            square_area = square_len * square_len
            print(f'The area of the square is {square_area:.2f}')
            print()
        elif choice == '2' :
            # Triangle
            tri_base = int(input('What is the base of the triangle : '))
            print(f'The input for the base : {tri_base}.')
            tri_ht = int(input('What is the height of the triangle : '))
            print(f'The input for the height : {tri_ht}.')
            tri_area = 1/2 * tri_base * tri_ht 
            print(f'The area of the triangle is {tri_area:.2f}')
            print()
        else :
            pass
            
