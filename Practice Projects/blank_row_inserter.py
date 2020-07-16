#! /usr/bin/env python3
# blank_row_inserter.py - Takes two integers and a filename string as command line arguments
# blank_row_inserter will start at the row (first int) and insert (second int) blank rows into the spreadsheet

import openpyxl
import sys


def insert_blank_row():
    # Assign variables
    file_name = sys.argv[3]
    beginning_row = int(sys.argv[1])
    num_of_rows = int(sys.argv[2])
    # Load workbook/sheet
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    # Insert blank rows
    sheet.insert_rows(beginning_row, amount=num_of_rows)
    # Save the file
    wb.save(f"new_{file_name}")


def main():
    insert_blank_row()


if __name__ == "__main__":
    main()
