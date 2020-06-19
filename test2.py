#! /usr/bin/env python3
# Deleting_unneeded_files.py will walk through a file tree
# Search for exceptionally large files or folders (filze size > 100MB)
# Print these files with their absolute path to the screen

from pathlib import Path
import os
from os.path import join, getsize


def delete_files_over_100mb(folder):
    # Get Path object for the folder
    # Walk the file tree
    for foldername, subfolders, filenames in os.walk(folder, followlinks=True):
        for filename in filenames:
            print(getsize(join(foldername, filename)))


delete_files_over_100mb("/home/comet")
