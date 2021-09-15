"""Write a program that categorizes each mail message by which day of the week the commit was done.

To do this look for lines that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print out the contents of your
dictionary (order does not matter).
"""
filename = input('Enter a file name: ')

try:
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\' + filename)
except:
    print('Unable to open the file named: ', filename)
    quit()

days = dict()
for line in fhand:
    words = line.split()
    if (len(words) < 3 or words[0] != 'From'):
        continue
    else:
        days[words[2]] = days.get(words[2], 0) + 1

print(days)
