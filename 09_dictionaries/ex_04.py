"""Add code to the above program to figure out who has the most messages in the file.

After all the data has been read and the dictionary has been created, look through the
dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who
has the most messages and print how many messages the person has.
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

print(max(emails), max(emails.values()))
