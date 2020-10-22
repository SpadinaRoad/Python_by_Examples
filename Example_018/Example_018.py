#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_018
# $ python3 Example_018.py
# $ python3 Example_018.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

018
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”.

"""

print(__doc__)

num = 1
while num != 0 : 
    num = int(input('Enter a number: '))
    print()
    print(f'Input for number : {num}')
    
    if num != 0 :
        if num < 10 :
            print(f'Too low.')
        elif num >= 10 and num <= 20 :
            print('Correct')
        else :
            print('Too high.')
    print()
    
