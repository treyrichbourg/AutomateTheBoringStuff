#! /usr/bin/env python3
# link_verification.py - Program that, given the URL of a web page, will attempt to download every linked page on the page.
# The program will flag any pages that have 404 "Not Found" status code and print them out as broken links.

import requests, bs4
import pyinputplus as pyip

# Download every linked page on a given url
def validate_links(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Capture all <a href> tags and get the hyperlink
    for link in soup.find_all('a'):
        link_elem = link['href']
        if 'https://' in link_elem:
            new_response = requests.get(link_elem)
            if new_response.status_code == 404:
                print(f"Broken Link: {link_elem}")
            else:
                pass
        else:
            print(f"{link_elem}")
            # new_response = requests.get(f"{url}/{link_elem}")
            # if new_response.status_code == 404:
            #     print(f"Broken Link: {link_elem}")
            # else:
            #     pass
    print(f"Checked all links in {url}")
validate_links('https://www.python.org')
# # Download every linked page on a given url
# def get_link_elem(url):
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     # Capture all <a href> tags and get the hyperlink
#     for link in soup.find_all('a'):
#         link_elem = link['href']
#     return link_elem

# def check_for_404(link):
#     print(link)

# def main(url):
#     hyperlink = get_link_elem(url)
#     check_for_404(hyperlink)

# main('https://www.python.org')