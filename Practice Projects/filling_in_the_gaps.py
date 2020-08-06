#! /usr/bin/env python3
# filling_in_the_gaps.py - Finds all files in a folder with a given prefix and locates any gaps in the numbering scheme.
# It will rename all the later files to close this gap in numbering.

from pathlib import Path
import shutil, re, sys

# Find all files in a folder with a given prefix
def rename_in_order():
    try:
        # Assign variable to folder path
        folder = Path(sys.argv[1])
        # Error handling for directory path
        if folder.is_dir() == False:
            print(f"{folder} is not a proper directory\nPlease enter a new path.")
        # Assign variable for prefix to search for
        prefix = sys.argv[2]
        # Find all files in folder with the given prefix
        files_to_renumber = list(folder.glob(f"{prefix}*"))
        # Sort files
        files_to_renumber.sort()
        number = 1
        for filename in files_to_renumber:
            # Partition the string name to remove extension
            name, _, ext = filename.name.partition(".")
            # Separate the prefix from the file number
            _, file_prefix, file_number = name.partition(prefix)
            # Rebuild new filename
            new_filename = Path(f"{folder}/{file_prefix}{str(number).zfill(3)}.{ext}")
            if filename == new_filename:
                pass
            number += 1
            # Rename the files in order
            shutil.move(filename, new_filename)
    except:
        print("Please enter a valid file path and name.")
    print(f"Your files in {folder} have been renamed.")


rename_in_order()
