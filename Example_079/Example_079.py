#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_079
# $ python3 Example_079.py
# $ python3 Example_079.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

079
Create an empty list called “nums”.
Ask the user to enter numbers.
After each number is entered, add
it to the end of the nums list and
display the list. Once they have
entered three numbers, ask them if
they still want the last number they
entered saved. If they say “no”,
remove the last item from the list.
Display the list of numbers.

"""

print(__doc__)

nums = []

for i in range(3) : 
    num_to_add = int(input('Enter a number : '))
    print(f'The input for a number: {num_to_add}')
    print()
    nums.append(num_to_add)
    print(f'The list of numbers : {nums}')
    print()
    
to_keep = input('Do you want the last number saved in the list? (y/n) ')
to_keep = to_keep.lower()
print(f'The input for keep : {to_keep}')
print()
if to_keep == 'n' :
    nums.remove(num_to_add)
print(f'The list of numbers : {nums}')    

