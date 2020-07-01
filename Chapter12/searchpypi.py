#! /usr/bin/env python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4

print("Searching...")  # Display text while downloading the search result page
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
link_elems = soup.select(".package-snippet")
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = f"https://pypi.org{link_elems[i].get('href')}"
    print("Opening", url_to_open)
    webbrowser.open(url_to_open)
