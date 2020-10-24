#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_033
# $ python3 Example_033.py
# $ python3 Example_033.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

033
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).

"""

print(__doc__)

int_a = ''
while int_a != 'x' : 
    int_a = input('Enter an integer : ')
    if int_a != 'x' : 
        int_a = int(int_a)
        int_b = input('Enter a second integer : ')
        int_b = int(int_b)

        print()
        print(f'The input for number 1 : {int_a}.')
        print(f'The input for number 2 : {int_b}.')

        print(f'{int_a} divided by {int_b} is {int_a // int_b} with {int_a % int_b} remaining.')
        print()
        
        
