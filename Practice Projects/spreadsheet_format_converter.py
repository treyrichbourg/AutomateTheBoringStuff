#! /usr/bin/env python3
# spreadsheet_format_converter.py - Takes a spreadsheet as an argument, uploads it to Google Sheets
# and copies the spreadsheet to other formats

import argparse
import ezsheets
import re
from pathlib import Path


def argument_parser():
    # One positional argument for the name of the spreadsheet to be manipulated
    # Rest of the arguments are optional
    # If no arguments are given the spreadsheet is simply uploaded to Google Drive
    parser = argparse.ArgumentParser(
        prog="Spreadsheet Converter",
        usage="%(prog)s [spreadsheet] [options]",
        description="Upload a spreadsheet to Google Drive and convert file type, if no optional arguements are given file is simply uploaded to Google Drive.\nIf a converted file already exists in the current directory it will be overwritten.",
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
    # Make sure file exists
    if Path(ss_name).absolute().exists() == False:
        raise Exception(f"{ss_name} was not found in current working directory.")
    sheet_list = ezsheets.listSpreadsheets()
    # Strip extension off ss_name
    ss_no_ext = re.sub(r"(\..*)", "", ss_name)
    # Check if spreadsheet is already in Google Drive, if not upload it.
    if ss_no_ext not in sheet_list.values():
        ss = ezsheets.upload(f"{ss_name}")
        return ss
    # If so, get the key and open it.
    else:
        for key, value in sheet_list.items():
            if ss_no_ext == value:
                ss = ezsheets.Spreadsheet(key)
                return ss


def optionals_given(var_args):
    optionals = 0
    keys = []
    for key in var_args:
        if var_args[key] == True:
            optionals += 1
            keys.append(key)
        else:
            optionals += 0
    formats = ", ".join(keys)
    if optionals >= 1:
        return (
            f"Converting {var_args['spreadsheet']} to the following formats: {formats}"
        )
    else:
        return f"{var_args['spreadsheet']} was uploaded to Google Drive."


def conditionals(args, ss):
    if args.csv:
        ss.downloadAsCSV()
    if args.excel:
        ss.downloadAsExcel()
    if args.zip:
        ss.downloadAsHTML()
    if args.pdf:
        ss.downloadAsPDF()
    if args.ods:
        ss.downloadAsODS()
    if args.tsv:
        ss.downloadAsTSV()


def main():
    # Parse Args
    args = argument_parser()
    # Feed ss_name to get_spreadsheet to either upload or open the spreadsheet depending on if it exists in Google Drive
    ss_name = args.spreadsheet
    print(f"Uploading {ss_name} to Google Drive...")
    ss = get_spreadsheet(ss_name)
    arg_dict = vars(args)
    # Give user progress on format conversion.
    optionals = optionals_given(arg_dict)
    print(optionals)
    # Run conditionals for every optional argument given
    conditionals(args, ss)
    print(f"Finished converting {ss_name}")


if __name__ == "__main__":
    main()

