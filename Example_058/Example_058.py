#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_058
# $ python3 Example_058.py
# $ python3 Example_058.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

058
Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five.

"""

import random

print(__doc__)

score = 0
count = 0
while count < 5 : 

    num_1 = random.randint(0,20)
    num_2 = random.randint(0,20)
    sum = num_1 + num_2
    answer = int(input(f'What is the sum of {num_1} and {num_2}? '))
    print(f'The input for the answer is {answer}.')
    print(f'The sum of {num_1} and {num_2} is {sum}.')
    if answer == sum : 
        print(f'Your answer is correct.')
        score += 1
    else : 
        print('Wrong answer.')
    count += 1
    print()
        
print(f'Your score is {score} out of 5.')
