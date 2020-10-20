#! /usr/bin/env python3
# formFiller.py - Automatically fills in the form. Form @ https://autbor.com/form

import pyautogui as pyag
import time

formData = [
    {
        "name": "Alice",
        "fear": "eavesdroppers",
        "source": "wand",
        "robocop": 4,
        "comments": "Tell Bob I said hi.",
    },
    {
        "name": "Bob",
        "fear": "bees",
        "source": "amulet",
        "robocop": 4,
        "comments": "n/a",
    },
    {
        "name": "Carol",
        "fear": "puppets",
        "source": "crystal ball",
        "robocop": 1,
        "comments": "Please take the puppets out of the break room.",
    },
    {
        "name": "Alex Murphy",
        "fear": "ED-209",
        "source": "money",
        "robocop": 5,
        "comments": "Protect the innocent. Serve the public trust. Uphold the law.",
    },
]

submitAnotherLink = (778, 232)

pyag.PAUSE = 0.5
print("Ensure that the browser window is active and the form is loaded!")

for person in formData:
    # Give the user a chance to kill the script.
    print(">>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<")
    time.sleep(5)

    print(f"Entering {person['name']} info...")
    pyag.write(["\t", "\t"])
    # Fill out the Name Field.
    pyag.write(person["name"] + "\t")
    # Fill out the Greatest Fear(s) field.
    pyag.write(person["fear"] + "\t")
    # Fill out the Source of Wizard Powers field.
    if person["source"] == "wand":
        pyag.write(["down", "enter", "\t"], 0.5)
    elif person["source"] == "amulet":
        pyag.write(["down", "down", "enter", "\t"], 0.5)
    elif person["source"] == "crystal ball":
        pyag.write(["down", "down", "down", "enter", "\t"], 0.5)
    elif person["source"] == "money":
        pyag.write(["down", "down", "down", "down", "enter", "\t"], 0.5)

    # Fill out the RoboCop field.
    if person["robocop"] == 1:
        pyag.write([" ", "\t", "\t"], 0.5)
    elif person["robocop"] == 2:
        pyag.write(["right", "\t", "\t"], 0.5)
    elif person["robocop"] == 3:
        pyag.write(["right", "right", "\t", "\t"], 0.5)
    elif person["robocop"] == 4:
        pyag.write(["right", "right", "right", "\t", "\t"], 0.5)
    elif person["robocop"] == 5:
        pyag.write(["right", "right", "right", "right", "\t", "\t"], 0.5)

    # Fill out the Additional Comments field.
    pyag.write(person["comments"] + "\t")

    # 'Click' Submit button by pressing Enter.
    time.sleep(0.5)
    pyag.press("enter")

    # Wait until form page has loaded.
    print("Submitted form.")
    time.sleep(5)

    # Click the Submit another response link.
    pyag.click(submitAnotherLink[0], submitAnotherLink[1])
