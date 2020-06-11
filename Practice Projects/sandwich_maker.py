#! Python3
# sandwich-maker.py will ask users for the sandwich preferences
import pyinputplus as pyip
import time, sys

while True:
    try:
        cost = 0
        print("Let's make a sandwich!\nPress 'ctrl + c' to exit")
        time.sleep(0.200)

        # Let user choose type of bread
        bread_choice = pyip.inputMenu(
            ["wheat", "white", "sourdough"],
            "Would you like wheat, white, or sourdough bread?\n",
        )
        if bread_choice == "sourdough":
            cost += 1.25
        else:
            cost += 1.00
        time.sleep(0.200)
        # Let user choose protein
        protein_choice = pyip.inputMenu(
            ["chicken", "turkey", "ham", "tofu"],
            "Would you like chicken, turkey, ham, or tofu?\n",
        )
        if protein_choice in ["chicken", "turkey", "ham"]:
            cost += 1.25
        else:
            cost += 0.75
        time.sleep(0.200)
        # Do they want cheese?
        cheese = pyip.inputYesNo("Would you like to add cheese?\n")
        if cheese == "yes":
            cheese_choice = pyip.inputMenu(
                ["cheddar", "Swiss", "mozzarella"],
                "Would you like cheddar, Swiss, or mozzarella?\n",
                caseSensitive=False,
            )
            if cheese_choice == "Swiss":
                cost += 1.25
            else:
                cost += 1.00
        # Do they want to add lettuce, tomato, mayo, mustard?
        condiment = pyip.inputYesNo(
            "Would you like to add mayo, mustard, lettuce or tomato?\n"
        )
        if condiment == "yes":
            cost += 0.50
        # How many sandwhiches to they want?
        sandwich_count = pyip.inputInt("How many sandwiches would you like?\n", min=1)
        cost *= sandwich_count
        print(f"Your total cost will be: ${cost}.")
        break
    # Allow keyboard interrupt to close the program without an error
    except KeyboardInterrupt:
        sys.exit()

