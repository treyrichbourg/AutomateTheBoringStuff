#! /usr/bin/env python3
# multiplication_table.py - Takes a number N from the cli and creates
# an N*N multiplication table in an Excel spreadsheet.

from openpyxl.styles import Font
import openpyxl
import sys

def create_table(n):
    bold_font = Font(bold=True)
    for i in range(1, n+1):
        sheet[f"A{i+1}"].font = bold_font
        sheet[f"A{i+1}"] = i
        sheet.cell(row=1, column=i+1).font = bold_font
        sheet.cell(row=1, column=i+1).value = i


def main():
    # Create Workbook and Worksheet objects, assign a variable to N, give sheet a title
    wb = openpyxl.Workbook()
    sheet = wb.active
    n = sys.argv[1]
    sheet.title = f'Multiplcation Table for {n}'
