"""Write a program to read through a mail log, build a histogram using a dictionary
to count how many messages have come from each email address, and print the
dictionary.

```
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
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
    if (len(words) < 3 or words[0] != 'From'):
        continue
    else:
        emails[words[1]] = emails.get(words[1], 0) + 1

print(emails)
