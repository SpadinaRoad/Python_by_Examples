#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_026
# $ python3 Example_026.py
# $ python3 Example_026.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

026
Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.

"""

print(__doc__)

a_word = ''
while a_word != 'x' : 
    a_word = input('Enter a word: ')
    if a_word != 'x' : 
        print(f'Input for a word : {a_word}')
        a_word = a_word.lower()
        if a_word[0] in 'aeiou' :
            print('We have a word starting in a vowel.')
            pig_latin = a_word + 'way'
            print(f'In pig latin, {a_word} is {pig_latin}')
        else :
            print('We have a word starting in a consonant.')
            pig_latin = a_word[1:] + a_word[0] + 'ay'
            print(f'In pig latin, {a_word} is {pig_latin}')
        print()
        
        
