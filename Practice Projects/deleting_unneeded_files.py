#! /usr/bin/env python3
# Deleting_unneeded_files.py will walk through a file tree
# Search for exceptionally large files or folders (filze size > 100MB)
# Print these files with their absolute path to the screen

from pathlib import Path
import os


def delete_files_over_100mb(folder):
    # Get Path object for the folder
    # Walk the file tree
    try:
        for foldername, _, filenames in os.walk(folder):

            for filename in filenames:
                # Get absolute path of the filename
                filename_abs = os.path.join(foldername, filename)
                # print(filename_abs)
                # If the file is > 100MB 'delete'(print) it to the screen
                if os.path.getsize(filename_abs) > 100000000:
                    print(
                        f"Size of {filename_abs} is {os.path.getsize(filename_abs)} deleting..."
                    )

    except:
        print("you done messed up")


delete_files_over_100mb("/home/comet/Games")

