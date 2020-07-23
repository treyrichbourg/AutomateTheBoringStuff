#! /usr/bin/env python3
# spreadsheet_format_converter.py - Takes a spreadsheet as an argument, uploads it to Google Sheets 
# and copies the spreadsheet to other formats

import argparse
import ezsheets
from pathlib import Path

