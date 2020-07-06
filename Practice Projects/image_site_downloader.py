#! /usr/bin/env python3
# image_site_downloader.py - This program goes to r/wallpapers
# searches a category and downloads the resulting images

import requests, bs4, os, praw
import pyinputplus as pyip
from pathlib import Path

reddit = praw.Reddit(
    client_id="6n8HaJ4i5jRaRA",
    client_secret="VhTYE2fKDIkD575w4GTniJCm1vk",
    redirect_uri="http://localhost:8080",
    user_agent="wallpaper_downloader by u/Comet_D_Monkey",
)

reddit = praw.Reddit(
    client_id="6n8HaJ4i5jRaRA",
    client_secret="VhTYE2fKDIkD575w4GTniJCm1vk",
    redirect_uri="http://localhost:8080",
    user_agent="wallpaper_downloader by u/Comet_D_Monkey",
)
print(reddit.auth.url(["identity"], "...", "permanent"))
