#! /usr/bin/env python3
# image_site_downloader.py - This program goes to r/wallpapers
# searches a category and downloads the resulting images

import requests, bs4, os, praw
import pyinputplus as pyip
from pathlib import Path


