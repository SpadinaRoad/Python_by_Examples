#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_042
# $ python3 Example_042.py
# $ python3 Example_042.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

042
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.

"""

print(__doc__)

total = 0
for i in range(5) : 

    num = input('Enter a number : ')
    print()
    print(f'The input for a number : {num}.')
    print()
    
    num = int(num)
    do_add = input(f'Add {num} to the total (Y/N)? : ')
    print()
    print(f'The input for question : {do_add}.')
    print()
    if do_add.lower() == 'y' :
        total += num

print(f'The total is: {total}')
    
