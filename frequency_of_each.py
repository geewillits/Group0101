# Find frequency of each word
# function for calculating the frequency
# Import regular expression module for Python
import re
#Input your text here
stringy = input('Enter your text string here: ')
stringier = (re.sub(r"\W+|_", " ", stringy))
str = stringier.upper()
# break the string into list of words
str_list = str.split()

unique = set(str_list)

for words in unique:
    print('Frequency of ', words, 'is :', str_list.count(words))
