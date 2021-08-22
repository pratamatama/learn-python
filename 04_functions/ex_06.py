"""
Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters
(hours and rate).
"""


def computepay(hours, rate):
    if (hours <= 40):
        return hours * rate
    return ((hours - 40) * (1.5 * rate)) + (40 * rate)


hours = int(input('Enter hours: '))
rate = float(input('Enter rate: '))
pay = computepay(hours, rate)

print('Pay: ' + str(pay))
