"""Write a program to look for lines of the form:

```
New Revision: 39772
```

Extract the number from each of the lines using a regular
expression and the findall() method. Compute the average
of the numbers and print out the average as an integer.

```
Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
```
"""
import re

filename = input('Enter file: ')

try:
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\' + filename)
except:
    print('Unable to open the file named: ', filename)
    quit()

count = 0
numbers = []
for line in fhand:
    number = re.findall('^New Revision: ([0-9]+)', line)
    if len(number) > 0:
        count += 1
        numbers.append(float(number[0]))

print(sum(numbers) / count)
