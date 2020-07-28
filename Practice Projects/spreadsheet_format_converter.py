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


def main():
    args = argument_parser()
    print(args)
    ss_name = args.spreadsheet
    print(ss_name)
    print(args.csv)
    ss = ezsheets.upload(f"{ss_name}")
    if args.csv:
        ss.downloadAsCSV(ss_name)
    # if args.excel:
    #     ss.downloadAsExcel(ss_name)
    # if args.zip:
    #     ss.downloadAsHTML(ss_name)
    # if args.pdf:
    #     ss.downloadAsPDF(ss_name)
    # if args.ods:
    #     ss.downloadAsODS(ss_name)
    # if args.tsv:
    #     ss.downloadAsTSV(ss_name)


if __name__ == "__main__":
    main()
