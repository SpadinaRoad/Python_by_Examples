#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_118
# $ python3 Example_118.py
# $ python3 Example_118.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

118
Define a subprogram that will ask the user to
enter a number and save it as the variable
“num”. Define another subprogram that will
use “num” and count from 1 to that number.

"""

print(__doc__)

def get_num() : 
    a_num = int(input('Enter a number : '))
    print(f'The input for a number : {a_num}')
    print()
    return a_num
    
def display_nums(a : 'number') :
    for i in range(1, a + 1) : 
        print(i)
    print()
    
a_num = get_num()
display_nums(a_num)

    
