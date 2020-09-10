#! /usr/bin/env python3
# sort_photo.py - Walk through a directory and search for jpg files.  Sort them into folders based on the date in the EXIF data.

from pathlib import Path
from PIL import Image
from PIL import ExifTags
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
    try:
        image = Image.open(filename)
        image.verify()
    except:
        return
    if image.getexif() == {}:
        print(f"{image.filename} has no exif data.")
        return  
    return image.getexif()

def sort_jpgs(path):
    for file in path.rglob('*.jpg' or '*.jpeg' or '*.JPG'):
        exif = get_exif(file)
        if exif == None: continue 
        exiftag = {ExifTags.TAGS[k]: v for k, v in exif.items() if k in ExifTags.TAGS and type(v) is not bytes}
        date_time_og = exiftag.get('DateTimeOriginal')
        if date_time_og != None:
            photo_date = re.match(r"20\d\d", exiftag['DateTimeOriginal']).group()
        else:
            photo_date = re.match(r"20\d\d", exiftag['DateTime']).group()
        Path(path/photo_date).mkdir(exist_ok=True)
        file_name = file.name
        source = Path(file)
        dest = Path(path/photo_date)
        if Path(dest/file_name).exists() == True: pass
        else:
            shutil.move(str(source), str(dest))    

def main():
    args = argument_parser()
    p = Path(args.path)
    sort_jpgs(p)


if __name__ == '__main__':
    main()