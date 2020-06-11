#! Python3
# date_detection.py uses regex to detect dates in a DD/MM/YYYY format
# stores them into variables named month, day and year
# validates if it is a valid date

import re

# Make one regex statement to catch the DD/MM/YYYY format
date_regex = re.compile(
    r"""(
    ([0-2][1-9]|1[0]|2[0]|3[01])  #capture the DD    
    (/)                           #/
    (0[1-9]|1[0-2])               #MM
    (/)                           #/
    ([12]\d{3})                   #YYYY
)""",
    re.VERBOSE,
)

# Write a function to validate the input as an actual date
def date_validator(text):
    try:
        # Assign variables
        date = date_regex.search(text)
        day, month, year = int(date.group(2)), int(date.group(4)), int(date.group(6))
        months_with_30_days = [4, 6, 9, 11]
        feb = 2
        leap = ""
        # Check for leap year
        if year % 4 == 0:
            leap = year
        elif year % 400 == 0:
            leap = year
        elif year % 100 == 0:
            leap = "no"
        if leap == year and month == feb:
            if day > 29:
                return "This date is not valid!"
        # Check months that only have 30 days
        if month in months_with_30_days and day > 30:
            return "This date is not valid!"
        # Everybody's favorite, February
        if leap == "no" and month == feb and day > 28:
            return "This date is not valid!"

        else:
            utcd, utcm, utcy = (date.group(2)), (date.group(4)), (date.group(6))
            print(date_regex.search(text).group())
            print(f"UTC {utcy}-{utcm}-{utcd}")

            return "This is a valid date!"
    except:
        return "Please enter a valid date."


print(date_validator("Is today 01/33/1960?"))
