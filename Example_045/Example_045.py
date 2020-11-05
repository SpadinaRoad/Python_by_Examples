#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_045
# $ python3 Example_045.py
# $ python3 Example_045.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

045
Set the total to 0 to start with. While the total is 50 or less, ask
the user to input a number. Add that number to the total and
print the message “The total is... [total]”. Stop the loop when
the total is over 50 .

"""

print(__doc__)

total = 0
while total <= 50 : 

    num = int(input('Enter a number : '))
    print()
    print(f'The input for a number : {num}.')
    
    total += num
    print(f'The total is {total}')
    print()
    
