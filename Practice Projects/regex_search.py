#!/usr/bin/env python3
# regex_search.py opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression
# The results are printed to the screen

from pathlib import Path
import re, os
import pyinputplus as pyip

# Prompt user to input a path to be searched
file_path = input("Please enter a path to the folder you want to search:\n")
file_path_obj = Path(file_path)  # Now we have the file path as a string and Path object

if Path.is_dir(file_path_obj) == True:  # Check for valid directory
    # Prompt user to input a regular expression
    search_criteria = pyip.inputRegexStr(
        prompt="Enter a regular expression to search for:\n"
    )
    text_files = os.listdir(file_path_obj)  # List all files in dir
    for text_file in text_files:  # Loop through all files
        try:  # This will prevent the program from crashing if it cannot open one of the files
            if text_file.endswith(".txt"):  # Find the text files
                contents = open(file_path_obj / text_file)  # Open the file
                list_of_lines = contents.readlines()  # Make a list of all the lines
                contents.close()  # Close the text file
                for (
                    line
                ) in list_of_lines:  # Loop through every item in the list of lines
                    if (
                        search_criteria.search(line) != None
                    ):  # If the regex str finds a match
                        print(
                            f"This line in {text_file} matched your regular expression search:\n{line}"
                        )
        except:
            print(f"The program was unable to open {contents}")  # Error handling
else:
    print("Please enter a valid file path.")
