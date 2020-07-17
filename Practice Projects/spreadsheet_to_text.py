#! /usr/bin/env python3
# spreadsheet_to_text.py - Open a spreadsheet and write the contents of one column to a text file
# write the cells of the next column to another text file and so on

import openpyxl
import sys
from pathlib import Path


def get_filename():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        filename = Path(filename).absolute()
        return filename


def spreadsheet_to_text(filename):
    # Open workbook
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    column_number = 1
    # Iterate over each column in the worksheet
    for column in range(sheet.max_column):
        try:
            # Open a text file
            new_filename = Path(
                f"{sys.argv[1].replace('.xlsx', '')}_{column_number}.txt"
            ).absolute()
            text_file = open(new_filename, "a")
            # Write content of each cell to a line in the file
            for cell_object in list(sheet.columns)[column]:
                text_file.write(f"{cell_object.value}\n")
            print(f"Saving file to {new_filename}")
            text_file.close()  # Close the text file
            column_number += 1
        except:
            print("Please enter a valid spreadsheet with .xlsx extension")


def main():
    filename = get_filename()
    spreadsheet_to_text(filename)


if __name__ == "__main__":
    main()
