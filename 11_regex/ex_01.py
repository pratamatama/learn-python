"""Write a simple program to simulate the operation of the grep command on Unix.

Ask the user to enter a regular expression and count the number of lines that
matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
"""
import re

regex = input('Enter a regular expression: ')
fhand = open(
    'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\mbox.txt')

count = 0
for line in fhand:
    if re.search(regex, line):
        count += 1

print('mbox.txt had ' + str(count) + ' lines that matched ' + regex)
