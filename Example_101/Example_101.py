#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_101
# $ python3 Example_101.py
# $ python3 Example_101.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

101
Using program 100, ask the user for a name and a region. Display the relevant data. Ask
the user for the name and region of data they want to change and allow them to make
the alteration to the sales figure. Display the sales for all regions for the name they
choose.

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

name = input('Enter a name : ')
print(f'The input for a name {name}')
print()

region = input('Enter a region : ')
print(f'The input for a region {region}')
print()

print(f'Sales for {name} in region {region} : {the_dict[name][region]}')
print()

sales = int(input('Enter new sales number: '))
print(f'The input for sales number: {sales}')
print()

the_dict[name][region] = sales
print(f'The sales for {name} : {the_dict[name]}')

