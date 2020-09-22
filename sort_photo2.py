#! /usr/bin/env python3
# sort_photo.py - Walk through a directory and search for jpg files.  Sort them into folders based on the date in the EXIF data.

from pathlib import Path
from PIL import Image
from PIL import ExifTags
import re
import shutil
import argparse
import logging

logging.basicConfig(filename="sort_log.log", level=logging.INFO)


def argument_parser():
    parser = argparse.ArgumentParser(
        prog="sort_photo.py",
        usage="%(prog)s [path]",
        description="Recursively search through a directory and sort photos based on date in exif data",
    )
    parser.add_argument("path", help="Enter the path you want to search through")
    args = parser.parse_args()
    return args


def get_exif(filename):
    try:
        image = Image.open(filename)
        image.verify()
    except Exception as e:
        logging.warning(f"Error: {e}\nError: Filename: {filename}")
        return
    if image.getexif() == {}:
        logging.warning(f"{image.filename} has no exif data.")
        return
    return image.getexif()


def sort_jpgs(path):
    for file in path.rglob("*.jpg" or "*.jpeg" or "*.JPG"):
        exif = get_exif(file)
        if exif == None:
            continue
        exiftag = {
            ExifTags.TAGS[k]: v
            for k, v in exif.items()
            if k in ExifTags.TAGS and type(v) is not bytes
        }

        # f = [exif.get(k) for k, v in ExifTags.TAGS.items() if v.startswith("Date")]

        date_time_og = exiftag.get("DateTimeOriginal")
        date_time = exiftag.get("DateTime")
        if date_time_og != None:
            photo_date = re.match(r"20\d\d", exiftag["DateTimeOriginal"]).group()
        elif date_time != None:
            photo_date = re.match(r"20\d\d", exiftag["DateTime"]).group()
        else:
            print(
                f"'DateTimeOriginal' or 'DateTime' are not valid exif keys in:\n{file}"
            )
            logging.debug(
                f"'DateTimeOriginal' or 'DateTime' are not valid exif keys in:\n{file}"
            )
        Path(path / photo_date).mkdir(exist_ok=True)
        file_name = file.name
        source = Path(file)
        dest = Path(path / photo_date)
        # print(f"source = {source}")
        logging.info(f"source = {source}")
        logging.info(f"destination = {dest/file_name}")
        # print(f"destination = {dest/file_name}")
        if Path(dest / file_name).exists() == True:
            pass
        else:
            shutil.move(str(source), str(dest))


def main():
    args = argument_parser()
    p = Path(args.path)
    sort_jpgs(p)


if __name__ == "__main__":
    main()
