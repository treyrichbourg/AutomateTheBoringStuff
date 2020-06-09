#! python3
# madlibs.py will read a text file and let the user replace the words ADJECTIVE, NOUN, ADVERB, or VERB wherever they appear.

from pathlib import Path
import re
import pyinputplus as pyip

#Open text file and copy contents to a variable as a string
text_file = open('./mad_lib.txt')
text_content = text_file.read()
text_file.close()
print(text_content)

#Search for the keywords ADJECTIVE, NOUN, ADVERB, and VERB
madlib_regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
words_to_repl = madlib_regex.findall(text_content)

#Prompt user and replace keywords
for word in range(len(words_to_repl)):
    text_content = text_content.replace(words_to_repl[word], pyip.inputStr(prompt = f"Enter {words_to_repl[word]}:\n"))
print(text_content)

#Print results and save the file
text_file = open('./mad_lib.txt', 'w')
text_file.write(text_content)
text_file.close()
