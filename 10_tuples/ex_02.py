"""This program counts the distribution of the hour of the day for each of the messages.

You can pull the hour from the “From” line by finding the time string and then splitting
that string into parts using the colon character. Once you have accumulated the counts
for each hour, print out the counts, one per line, sorted by hour as shown below.

```
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
```
"""
filename = input('Enter a file name: ')

try:
    fhand = open(
        'C:\\Users\\Rin\\Documents\\Learn\\py4e\\09_dictionaries\\' + filename)
except:
    print('Unable to open the file named: ', filename)
    quit()

hours = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        hour = words[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

lst = []
for key, val in list(hours.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
