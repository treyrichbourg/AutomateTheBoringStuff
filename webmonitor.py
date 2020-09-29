import smtplib
import requests
import sys

try:
    r = requests.get('https://www.reddit.com/fakesite')
except Exception as err:
    print(err)
email = 'email'
if r.status_code != 200:
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)  #your email server smtp server.
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(email, sys.argv[1]) #sys.argv[1] will be your password, passed to the script as a cli argument.
    body = f"Subject: Your website is down!"
    print(f"Sending email to {email}...")
    sendmail_status = smtp_obj.sendmail(email, email, body) #email is used twice because you are sending an email to yourself.

    if sendmail_status != {}:
        print(f"There was a problem sending email to {email}: {sendmail_status}")
smtp_obj.quit()
