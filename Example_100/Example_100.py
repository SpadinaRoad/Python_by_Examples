#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_100
# $ python3 Example_100.py
# $ python3 Example_100.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

100
Create the following using a 2D dictionary showing
the sales each person has made in the different
geographical regions:

         N       S       E       W
John    3056    8463    8441    2694
Tom     4832    6786    4737    3612
Anne    5239    4802    5820    1859
Fiona   3904    3645    8821    2451
    
"""

print(__doc__)

the_dict = {
    'John'  : {'n' : 3056, 's' : 8463, 'e' : 8441, 'w' : 2694}, 
    'Tom'   : {'n' : 4832, 's' : 6786, 'e' : 4737, 'w' : 3612}, 
    'Anne'  : {'n' : 4128, 's' : 4802, 'e' : 5820, 'w' : 1859}, 
    'Fiona' : {'n' : 3904, 's' : 3645, 'e' : 8821, 'w' : 2451}, 
}

print(the_dict)
print()

print(f'Sales by John : {the_dict["John"]}')
print(f'Sales by John in e: {the_dict["John"]["e"]}')
print()
