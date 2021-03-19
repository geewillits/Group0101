# Find frequency of each word
# function for calculating the frequency
# Import regular expression module for Python
import re
#Input your text here
stringy = input('Enter your text string here: ')
#Use Regex to replace all non-word characters
stringier = (re.sub(r"\W+|_", " ", stringy))
#Convert to upper case to avoid counting differently capitalized words seperately
str = stringier.upper()
# break the string into list of words
str_list = str.split()
#delivers set of unique words
unique = set(str_list)
#counts each word in the unique list in the master list. boomtown
for words in unique:
    print('Frequency of ', words, 'is :', str_list.count(words))
