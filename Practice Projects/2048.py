#! /usr/bin/env python3
# 2048.py - Opens Firefox browser, connects to https://play2048.co and automatically plays the game
# this script uses selenium and simply sends up, right, down, left keystrokes.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def play_2048():
    browser = webdriver.Firefox()  # Open browser
    browser.get("https://play2048.co")  # Go to the website to play 2048
    game_board = browser.find_element_by_css_selector('body')
    while True:
        game_board.send_keys(Keys.UP)
        time.sleep(.2)
        game_board.send_keys(Keys.RIGHT)
        time.sleep(.2)
        game_board.send_keys(Keys.DOWN)
        time.sleep(.2)
        game_board.send_keys(Keys.LEFT)
        time.sleep(.2)

play_2048()