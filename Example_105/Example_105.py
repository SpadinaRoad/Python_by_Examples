#!/usr/bin/python3
# -*- coding: utf-8 -*-

# To run in terminal
# $ cd /home/james/Documents/Edoc/3Nohtyp/Python_By_Example/Example_105
# $ python3 Example_105.py
# $ python3 Example_105.py <Input.txt >Output.txt

"""
Python by Example: Learning to Program in 150 Challenges by Nichola Lacey

105
Write a new file
called
“Numbers.txt”.
Add five numbers
to the document
which are stored
on the same line
and only
separated by a
comma. Once you
have run the
program, look in
the location where
your program is
stored and you
should see that
the file has been
created. The
easiest way to
view the contents
of the new text file
on a Windows
system is to read it
using Notepad.
    
"""

print(__doc__)

with open('Numbers.txt', 'w') as fo :
    fo.write('1, 2, 3, 4, 5\n')

    
    
