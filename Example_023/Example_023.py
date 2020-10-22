#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_023
# $ python3 Example_023.py
# $ python3 Example_023.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).

"""

print(__doc__)

text = ''
while text != 'x' : 
    text = input('Enter the first line of a nursery rhyme: ')
    print()
    print(f'Input for nursery rhyme : {text}')
    if text != 'x' : 
        t_len = len(text)
        print(f'The length of the text is {t_len}.')

        start = int(input('Enter a starting number : '))
        print(f'Input for starting number : {start}')
        print()

        if start in range(0, t_len) :
            end = int(input('Enter an ending number : '))
            print(f'Input for ending number   : {end}')
            print()
            if start <= end : 
                if end in range(0, t_len) :
                    print(f'The string segment: {text[start:end]}')
                    print()
                else :
                    print(f'The end number should be from 0 to {t_len}.')
                    print()
            else :
                print(f'The start value {start} should be before {end}')
                print()
        else :
            print(f'The start number should be from 0 to {t_len}.')
            print()

            
