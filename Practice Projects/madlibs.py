#! python3
# madlibs.py will read a text file and let the user replace the words ADJECTIVE, NOUN, ADVERB, or VERB wherever they appear.

from pathlib import Path
import os, re
import pyinputplus as pyip

#Open text file and copy contents to a variable as a string
text_file = open('./mad_lib.txt')
text_content = text_file.read()
text_file.close()
print(text_content)
#Search for the keywords ADJECTIVE, NOUN, ADVERB, and VERB
#key = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
madlib_regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
words_to_repl = madlib_regex.findall(text_content)
#print(words_to_repl)
#Prompt user and replace keywords
for word in range(len(words_to_repl)):
    text_content = text_content.replace(words_to_repl[word], pyip.inputStr(prompt = f"Enter {words_to_repl[word]}:\n"))
print(text_content)
#Print results and save the file
text_file = open('./mad_lib.txt', 'w')
text_file.write(text_content)
text_file.close()

# adjective_repl = pyip.inputStr(prompt = 'Enter an adjective:\n')
# noun_repl = pyip.inputStr(prompt = 'Enter a noun:\n')
# adverb_repl = pyip.inputStr(prompt = 'Enter an adverb:\n')
# verb_repl = pyip.inputStr(prompt = 'Enter an adjective:\n')
#Prompt user to replace the keywords
# for word in text_content:
#     if word in key:
#         if word == key[0]:
#             adjective_repl = pyip.inputStr(prompt = 'Enter an adjective:\n')
#             text_content = text_content.replace(key[0], adjective_repl)
#             print(text_content)
#         if word == key[1]:
#             noun_repl = pyip.inputStr(prompt = 'Enter a noun:\n')
#             text_content = text_content.replace(key[1], noun_repl)
#             print(text_content)
#         if word == key[2]:
#             adverb_repl = pyip.inputStr(prompt = 'Enter an adverb:\n')
#             text_content = text_content.replace(key[2], adverb_repl)
#             print(text_content)
#         if word == key[3]:
#             verb_repl = pyip.inputStr(prompt = 'Enter an adjective:\n')
#             text_content = text_content.replace(key[3], verb_repl)
# print(text_content)


        

#Replace keywords


#Print results and save the file