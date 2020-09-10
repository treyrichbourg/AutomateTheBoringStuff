#! /usr/bin/env python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue    # skip non-csv files

    print(f"Removing header from {csv_filename}...")

    # TODO: Read the CSV file in (skipping first row).
    csv_rows = []
    csv_file_obj = open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)
    csv_rows_comp = [row for row in reader_obj if reader_obj.line_num != 1]
    # print(csv_rows_comp)
    # for row in csv_rows_comp:
    #     print(row)
    # for row in reader_obj:
    #     if reader_obj.line_num == 1:
    #         continue    # skip the first row
    #     csv_rows.append(row)
    csv_file_obj.close()
    # TODO: Write out the CSV file.
    csv_file_obj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)
    for row in csv_rows_comp:
        csv_writer.writerow(row)
    csv_file_obj.close()