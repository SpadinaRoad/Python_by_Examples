#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_075
# $ python3 Example_075.py
# $ python3 Example_075.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

075
Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”

"""

print(__doc__)


num_list = [671, 943, 480, 534]
for i in num_list :
    print(f'The number is : {i}')
print()

choice = int(input('Enter a three-digit number: '))
print(f'Input for the number: {choice}')
print()

if choice in num_list : 
    print(f'The index for the number is {num_list.index(choice)}')
else :
    print('That number is not in the list.')

