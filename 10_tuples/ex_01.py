"""Revise a previous program as follows: Read and parse the “From” lines
and pull out the addresses from the line.

Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.

```
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
```
"""
filename = input('Enter a file name: ')

try:
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\' + filename)
except:
    print('Unable to open the file named: ', filename)
    quit()

emails = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        emails[words[1]] = emails.get(words[1], 0) + 1

lst = []
for key, val in list(emails.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(val, key)
