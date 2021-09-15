"""Figure out which line of the above program is still not properly guarded.
See if you can construct a text file which causes the program to fail and
then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.
"""

fhand = open('C:\\Users\\Rin\\Documents\\Learn\\py4e\\08_lists\\mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if (len(words) == 0 or len(words) < 3):
        continue
    if (words[0] != 'From'):
        continue
    print(words[2])