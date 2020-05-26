#!/usr/bin/env python3

#mclip.pi - A multi-clipboard program.

import sys, pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

#Exits the script if the user does not add a keyphrase
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

#sys.argv[1] could be used as well but 'keyphrase' makes the script more readable
keyphrase = sys.argv[1]   #first command line arg is the keyphrase

#looks for the keyphrase (sys.argv[1]) in the dictionary TEXT and copies the value to the clipboard
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard.")
else:
    print(f"There is no text for {keyphrase}")
