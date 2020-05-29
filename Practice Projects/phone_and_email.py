#! python3
#phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)? #space or separator
    (\d{3}) #first 3 digits of phone number
    (\s|-|\.) #separator
    (\d{4}) #end of phone number
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension, if applicable
    )''', re.VERBOSE)

#Create email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-z]{2,4})
    )''', re.VERBOSE)

#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += f" x{groups[8]}"
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
