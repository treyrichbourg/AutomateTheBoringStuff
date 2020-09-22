#! /usr/bin/env python3
# text_myself.py - Defines the text_myself() function that texts a message passed to it as a string.

# Preset values:
account_SID = ""
auth_token = ""
my_number = ""
twilio_number = ""

from twilio.rest import Client


def text_myself(message):
    twilio_cli = Client(account_SID, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)

