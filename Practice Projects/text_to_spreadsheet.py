#! /usr/bin/env python3
# text_to_spreadsheet.py - Opens serveral text files and inserts the contents
# into a spreadsheet with one line per row and
# one column per file

import openpyxl
import sys
from pathlib import Path


def get_path():
    path = Path(sys.argv[1]).absolute()
    if path.is_dir():
        return path
    else:
        print(f"{path} is not a valid path!")


def get_content(path):
    # Grab files in current dir
    files = list(path.glob("*.txt"))
    content_meta = []
    # Loop through the text files in current directory, open them and get content
    for file in files:
        file = open(file)
        content = file.readlines()
        content_meta.append(content)
    print(content_meta)
    return content_meta


def text_to_spreadsheet(path):
    # Open workbook
    wb = openpyxl.Workbook()
    sheet = wb.active
    # Get list of Path objects for each file
    files = list(path.glob("*.txt"))
    # Iterate over each object in the list to get the number of columns
    # Each file represents a column
    for column in range(1, len(files) + 1):
        file = files[column - 1]
        file = open(file)
        # Get the content from each line in 'file'
        # This will also represent each row in the spreadsheet
        content = file.readlines()
        for row in range(1, len(content) + 1):
            sheet.cell(row=row, column=column).value = content[row - 1]
    print(f"Saving file to {path}/text2sheet.xlsx")
    wb.save(f"{path}/text2sheet.xlsx")


def main():
    path = get_path()
    text_to_spreadsheet(path)


if __name__ == "__main__":
    main()

