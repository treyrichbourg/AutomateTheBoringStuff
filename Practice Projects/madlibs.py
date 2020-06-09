#! python3
# madlibs.py will read a text file and let the user replace the words ADJECTIVE, NOUN, ADVERB, or VERB wherever they appear.

from pathlib import Path
import os, re

#Open text file
text_file = open(Path.cwd() / 'mad_lib.txt')
text_content = text_file.read()
print(text_content)
#Search for the keywords ADJECTIVE, NOUN, ADVERB, and VERB
madlib_regex = re.compile(r'(ADJECTIVE)|(NOUN)|(ADVERB)|(VERB)')
for words in madlib_regex.findall(text_content):
    print(words)
#Prompt user to replace the keywords

#Replace keywords

#Print results and save the file