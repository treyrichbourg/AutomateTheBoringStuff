#! /usr/bin/env python3
# selective-copy.py - Walk through a folder tree and search for files with a certain file extension.
# Copy these files from whatever location they are in to a new folder.

import os, shutil, re
from pathlib import Path


def selective_copy(folder, destination):

    # folder = Path(folder)
    # destination = Path(destination)
    extension = input("Enter a file extension to search for:\n")
    # Walk through folder tree and grab all files that end with extension entered
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                # print(filename)
                shutil.copy(os.path.join(foldername, filename), destination)


selective_copy(
    "/mnt/c/Users/trey/Documents/delicious", "/mnt/c/Users/trey/Documents/test"
)

