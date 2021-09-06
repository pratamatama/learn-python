"""Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter
Egg to their program. Modify the program that prompts the user for the file name so that it
prints a funny message when the user types in the exact file name “na na boo boo”. The program
should behave normally for all other files which exist and don’t exist. Here is a sample
execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.
"""
try:
    filename = input('Enter the file name: ')

    if filename == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        quit()

    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\07_files\\' + filename)

    lines_count = 0
    for line in fhand:
        if not line.startswith('Subject:'):
            continue
        lines_count = lines_count + 1
    print('There were ' + str(lines_count) + ' subject in ' + filename)
except:
    print('File cannot be opened: ' + filename)
    quit()
