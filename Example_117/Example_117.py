#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_117
# $ python3 Example_117.py
# $ python3 Example_117.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

117
Create a simple maths quiz that will ask the user for their name and then generate two
random questions. Store their name, the questions they were asked, their answers and
their final score in a .csv file. Whenever the program is run it should add to the .csv file
and not overwrite anything.

"""

import csv
import random

print(__doc__)

#Start data.
print('The Great Math Quiz')
print('')

name = input('What is your name? ')
print(f'The input for name: {name}')
print()

#Saving to csv file
filename = 'MathQuiz.csv'
with open(filename, 'a') as fo:
    fo.write('The Great Math Quiz\n')
    fo.write(f'User: {name}\n')
    fo.write('\n')
    
#First math question.
operand_a = random.randint(1, 100)
operand_b = random.randint(1, 100)

correct_answer = operand_a + operand_b
line_1 = f'Enter the addition of {operand_a} and {operand_b} : '
answer = int(input(line_1))
line_2 = f'Your answer is {answer}. '
if answer == correct_answer :
    line_2 += 'It is correct.'
    score = 1
else : 
    line_2 += 'It is not correct.'
    score = 0
print(line_2)

with open(filename, 'a') as fo :
    fo.write('The first question: \n')
    fo.write(f'{line_1}\n')
    fo.write(f'{line_2}\n')
    fo.write(f'\n')
print()
    
#Second math question.
operand_a = random.randint(1, 100)
operand_b = random.randint(1, 100)

correct_answer = operand_a + operand_b
line_1 = f'Enter the addition of {operand_a} and {operand_b} : '
answer = int(input(line_1))
line_2 = f'Your answer is {answer}. '
if answer == correct_answer :
    line_2 += 'It is correct.'
    score += 1
else : 
    line_2 += 'It is not correct.'
    score += 0
print(line_2)

with open(filename, 'a') as fo :
    fo.write('The first question: \n')
    fo.write(f'{line_1}\n')
    fo.write(f'{line_2}\n')
    fo.write(f'\n')
    fo.write(f'Correct answers: {score} out of 2 ({score/2:.2%}).')


print()


