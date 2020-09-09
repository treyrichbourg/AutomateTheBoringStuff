#! /usr/bin/env python3
# sort_photo.py - Walk through a directory and search for jpg files.  Sort them into folders based on the date in the EXIF data.

from pathlib import Path
from PIL import Image
import re
import shutil
import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
        prog="sort_photo.py",
        usage="%(prog)s [path]",
        description="Recursively search through a directory and sort photos based on date in exif data"
    )
    parser.add_argument("path", help="Enter the path you want to search through")
    args = parser.parse_args()
    return args

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def sort_jpgs(path):
    for file in path.rglob('*.jpg'):
        exif = get_exif(file)
        photo_date = re.match(r"20\d\d", exif[36867]).group()
        Path(path/photo_date).mkdir(exist_ok=True)
        source = str(path/file)
        dest = str(path/photo_date)
        shutil.move(source, dest)    

def main():
    args = argument_parser()
    p = Path(args.path)
    sort_jpgs(p)


if __name__ == '__main__':
    main()