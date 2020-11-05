#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_046
# $ python3 Example_046.py
# $ python3 Example_046.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

046
Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program.

"""

print(__doc__)

num = 0
while num <= 5 : 

    num = int(input('Enter a number : '))
    print()
    print(f'The input for a number : {num}.')
    
print(f'The last number you entered was {num}')
print()
    
