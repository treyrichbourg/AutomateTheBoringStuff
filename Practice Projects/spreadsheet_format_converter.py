#! /usr/bin/env python3
# spreadsheet_format_converter.py - Takes a spreadsheet as an argument, uploads it to Google Sheets
# and copies the spreadsheet to other formats

import argparse
import ezsheets
from pathlib import Path

# Parse Args
# Upload spreadsheet
# use downloadAsArg()


def argument_parser():
    # One positional argument for the name of the spreadsheet to be manipulated
    # Rest of the arguments are optional 
    # If no arguments are given the spreadsheet is simply uploaded to Google Drive
    parser = argparse.ArgumentParser(
        prog="Spreadsheet Converter",
        usage="%(prog)s [spreadsheet] [options]",
        description="Upload a spreadsheet to Google Drive and convert file type",
    )
    parser.add_argument(
        "spreadsheet", help="Enter the name of the spreadsheet to upload."
    )
    parser.add_argument(
        "-c",
        "--csv",
        action="store_true",
        help="only downloads the first sheet as a csv file",
    )
    parser.add_argument(
        "-e", "--excel", action="store_true", help="downloads the file as an Excel file"
    )
    parser.add_argument(
        "-z",
        "--zip",
        "--html",
        action="store_true",
        help="download a zip of HTML files",
    )
    parser.add_argument(
        "-p", "--pdf", action="store_true", help="download the spreadsheet as a PDF"
    )
    parser.add_argument(
        "-o",
        "--ods",
        action="store_true",
        help="downloads the spreadsheet as an OpenOffice file",
    )
    parser.add_argument(
        "-t",
        "--tsv",
        action="store_true",
        help="only downloads the first sheet as a TSV file",
    )
    args = parser.parse_args()
    return args

def get_spreadsheet(ss_name):
    sheet_list = ezsheets.listSpreadsheets()
    if ss_name not in sheet_list.values():
        ss=ezsheets.upload(f"{ss_name}")
        return ss
    else:
        for key, value in sheet_list.items():
            if ss_name == value:
                ss = ezsheets.Spreadsheet(key)
                return ss
            else:
                raise Exception('The given spreadsheet name could not be uploaded and was not found in Google Drive.')
    

def main():
    args = argument_parser()
    # ss_name = args.spreadsheet
    # ss = get_spreadsheet(ss_name) 
    # print(f'Converting {ss_name}...')
    optional_args = []
    arg_dict = vars(args)
    for key in arg_dict.keys():
        if key != 'spreadsheet':
            optional_args.append(key)
    print(optional_args)
    #print(vars(args))
    # if args.csv:
    #     ss.downloadAsCSV() 
    # if args.excel:
    #     ss.downloadAsExcel()
    # if args.zip:
    #     ss.downloadAsHTML()
    # if args.pdf:
    #     ss.downloadAsPDF()
    # if args.ods:
    #     ss.downloadAsODS()
    # if args.tsv:
    #     ss.downloadAsTSV()
    # print(f"Finished converting {ss_name}")
    #print(args)
if __name__ == "__main__":
    main()
