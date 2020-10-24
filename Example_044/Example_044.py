#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_044
# $ python3 Example_044.py
# $ python3 Example_044.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

044
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.

"""

print(__doc__)

num = ''
while num != 'x' : 

    num = input('How many to invite to your party? ')
    print()
    print(f'The input for a number : {num}.')
    
    if num != 'x' : 
        num = int(num)
        if num < 10 :
            for i in range(num) :
                name = input('What is the person\'s name? ')
                print(f'{name} has been invited.')
        else :
            print('Too many people')
        print()
