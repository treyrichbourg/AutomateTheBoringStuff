#! /usr/bin/env python3
# cmd_line_emailer.py - Takes an email address and string of text
# on the command line and then logs into your email account
# and sends an email of the string to the provided address.

import sys, requests, time
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Take an email address and string of text as sysargv and assign them to variables
recipient = sys.argv[1]
email_body = sys.argv[2]


def prompt():
    # Ask user for their email and password
    global sender
    global sender_pass
    sender = pyip.inputEmail(prompt="Please enter your email:\n")
    sender_pass = pyip.inputPassword(prompt="Enter your password:\n", mask="*")


# Create a new email and fill out the form
def launch_gmail():
    global browser
    # Log into email address
    browser = webdriver.Firefox()  # Open browser
    browser.get("https://mail.google.com/mail")  # Go to gmail sign in page
    user_elem = browser.find_element_by_class_name(
        "whsOnd.zHQkBf"
    )  # Select the username form
    user_elem.send_keys(sender)  # Enter email address
    user_elem.send_keys(Keys.ENTER)
    time.sleep(1)
    passwd_elem = browser.find_element_by_class_name(
        "whsOnd.zHQkBf"
    )  # Select the password field
    passwd_elem.send_keys(sender_pass)  # Enter password
    passwd_elem.send_keys(Keys.ENTER)
    time.sleep(3)
    # Congrats you are now logged into your e-mail portal!


def send_email():
    compose_elem = browser.find_element_by_class_name(
        "T-I.T-I-KE.L3"
    )  # Compose a new email
    compose_elem.click()
    time.sleep(1)
    to_elem = browser.find_element_by_id(":9m")  # Select the 'To' field
    to_elem.send_keys(recipient)
    time.sleep(0.75)
    body_elem = browser.find_element_by_id(":a9")  # Select the 'Body' field
    body_elem.send_keys(email_body)
    time.sleep(0.75)
    send_elem = browser.find_element_by_class_name(
        "T-I.J-J5-Ji.aoO.v7.T-I-atl.L3"
    )  # Find the 'Send' button
    send_elem.click()


def main():
    prompt()
    launch_gmail()
    send_email()


main()
