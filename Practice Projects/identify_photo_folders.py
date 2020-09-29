#! /usr/bin/env python3
'''
identify_photo_folders.py uses os.walk() to look through a directory and decide if the folder is comprised of 
50% or more photo files
'''
import os
from PIL import Image
from pathlib import Path
import sys


path = Path(sys.argv[1])

for foldername, subfolders, filenames in os.walk(path):
    num_photo_files = 0
    num_non_photo_files = 0
    
    for filename in filenames:
        if not filename.lower().endswith(('.jpg', '.png')):
            num_non_photo_files += 1
            continue
        #print(Path(filename).absolute())
        image_file = Image.open(os.path.join(foldername, filename))
        height, width = image_file.size

        if height and width > 500:
            num_photo_files += 1
        else:
            num_non_photo_files += 1
    
    if num_photo_files > ((num_photo_files + num_non_photo_files) / 2):
        print(Path(foldername).absolute())

        