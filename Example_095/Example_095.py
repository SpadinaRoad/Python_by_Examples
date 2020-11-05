#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_095
# $ python3 Example_095.py
# $ python3 Example_095.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

095
Create an array of five numbers
between 10 and 100 which each have
two decimal places. Ask the user to
enter a whole number between 2 and 5.
If they enter something outside of that
range, display a suitable error message
and ask them to try again until they
enter a valid amount. Divide each of the
numbers in the array by the number the
user entered and display the answers
shown to two decimal places.

"""

from array import *
import random

print(__doc__)

array_rand = array('f', [])
print('Here is a list of random two-decimal numbers: ')
for i in range(5) :
    rand_num = random.randint(1000, 10000)
    rand_num = rand_num / 100
    array_rand.append(rand_num)
    print(f'{rand_num:.2f}')
print()

user_num = 0
while user_num < 2 or user_num > 5 : 
    user_num = int(input('Enter a number between 2 and 5: '))
    print(f'The input for the divisor {user_num}')
    print()
    if user_num < 2 or user_num > 5 :
        print('Your selection is out of range.')
    else : 
        print(f'The numbers divided by {user_num}: ')
        for i in range(5) : 
            div_num = array_rand[i] / user_num
            print(f'{div_num:.2f}')
            



