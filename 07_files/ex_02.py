"""Write a program to prompt for a file name, and then
read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print
out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.
"""
try:
    filename = input('Enter a file name: ')
    lines_count = 0
    confidences = 0
    lookup = 'X-DSPAM-Confidence:'
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\07_files\\' + filename)
    for line in fhand:
        if not line.startswith(lookup):
            continue
        lines_count = lines_count + 1
        confidences += float(line[len(lookup):-1].strip())
    print('Average spam confidence: ', confidences/lines_count)
except:
    print('File could not be opened:', filename)
