#! /usr/bin/env python3
# filling_in_the_gaps.py - Finds all files in a folder with a given prefix and locates any gaps in the numbering scheme.
# It will rename all the later files to close this gap in numbering.

from pathlib import Path
import shutil, re, os, sys


def rename_in_order():
    # Make a regex to grab the numbers
    number_pattern = re.compile(r"(00\d)|(0\d\d)|(\d\d\d)")
    # Assign variable to folder path
    folder = Path(sys.argv[1])
    # Assign variable for prefix to search for
    prefix = sys.argv[2]
    # Find all files in folder with the given prefix
    files_to_renumber = list(folder.glob(f"{prefix}*"))
    # Sort files
    files_to_renumber.sort()
    # Do a regex search to find the numbers after the prefix and before the file extension
    file_numbers = [
        number_pattern.search(filename.name).group() for filename in files_to_renumber
    ]
    # print(file_numbers)
    for filename in files_to_renumber:
        number = number_pattern.search(filename.name).group()
        print(number)
        print(filename.name)
    # print(file_numbers)
    # for filename in files_to_renumber:
    #     name, _, ext = filename.name.partition(".")
    #     new_filename = f"{folder}/{prefix}.{ext}"
    # print(new_filename)


rename_in_order()
