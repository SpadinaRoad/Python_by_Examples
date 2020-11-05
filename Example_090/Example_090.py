#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_090
# $ python3 Example_090.py
# $ python3 Example_090.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

090
Ask the user to enter numbers. If they enter a
number between 10 and 20, save it in the array,
otherwise display the message “Outside the
range”. Once five numbers have been
successfully added, display the message “Thank
you” and display the array with each item shown
on a separate line.

"""

from array import *

print(__doc__)

int_array = array('i', [])

count = 0
while count < 5 :
    a_num = int(input('Enter a number between 10 and 20 : '))
    print(f'The input for a number: {a_num}')
    if a_num >= 10 and a_num <= 20 :
        int_array.append(a_num)
        count += 1
    else : 
        print('The number is outside the range.')
    print()
    
print('Thank you.')
print()
for i in int_array :
    print(i)
    
        
        
