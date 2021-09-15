"""Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
"""
count = 0
dictionary = {}
try:
    filename = input('Enter a file name: ')
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\' + filename)
    for line in fhand:
        words = line.split()
        for word in words:
            count += 1
            if word in dictionary:
                continue
            dictionary[word] = count
except:
    print('Unable to open the file named: ', filename)
    quit()

if 'Writing' in dictionary:
    print('True')
else:
    print('False')
