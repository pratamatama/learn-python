"""Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string
after the colon character and then use the float function to convert
the extracted string into a floating point number.
"""
words = 'X-DSPAM-Confidence: 0.8475'
colon_pos = words.find(':')
float_str = words[colon_pos + 1:]
float_pts = float(float_str)

print(float_pts)
