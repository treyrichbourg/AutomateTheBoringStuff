#! Python3
# regex_strip.py does the same thing as the strip() string method
import re

# write a regex statement to remove whitespace from the beginning and end of string
strip_regex = re.compile(r"\S.+\S")
anything_regex = re.compile(r".+")

# Write a function that performs the same as strip() method using regex.
# If a second arguement is passed remove it from the string instead
def strip(string_to_strip, anything=None):
    if anything == None:
        string_to_strip = strip_regex.search(string_to_strip).group()
        print(string_to_strip)
    else:
        # original code to filter the 'anything' arg from the string
        # remove_this = anything_regex.search(anything).group()
        # string_to_strip = string_to_strip.split(str(remove_this))
        # print(' '.join(string_to_strip))
        # new solution using re.sub()
        result = re.sub(anything, "", string_to_strip)
        print(result)


string_with_whitespace = "  I need to be stripped    "

strip(string_with_whitespace)
strip(string_with_whitespace, "e")
