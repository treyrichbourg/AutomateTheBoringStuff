#! /usr/bin/env python3
# link_verification.py - Program that, given the URL of a web page, will attempt to download every linked page on the page.
# The program will flag any pages that have 404 "Not Found" status code and print them out as broken links.

import requests
import bs4

# All in one solution to the problem in a single function
def validate_links(url):
    # Download url, check status, parse HTML
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # Capture all <a href> tags and get the hyperlink
    for link in soup.find_all("a", href=True):
        link_elem = link["href"]
        if "http" in link_elem:
            new_response = requests.get(link_elem)
            status = new_response.status_code
            if status == 404:
                print(f"{res.url} returned a status code of {status} 'Not Found'.")
            else:
                pass
    print(f"Checked all links in {url}")


# Problem broken down
def capture_link_elem(url):
    # Download url, check status, parse HTML, create list to hold links to other websites
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    website_links = []
    # Capture all the link elements that lead to another website
    for hyperlink in soup.find_all("a", href=True):
        link_elem = hyperlink["href"]
        if "http" in link_elem:
            website_links.append(link_elem)
    return website_links


def verify_link(list_of_links):
    # Loop through every link in the list, grab status code and check for 404
    for link in list_of_links:
        res = requests.get(link)
        status = res.status_code
        if status == 404:
            print(f"{res.url} returned a status code of {status} 'Not Found'.")
        else:
            pass


def main(url):
    list_of_links = capture_link_elem(url)
    verify_link(list_of_links)
    print("All links have been verified")


main("https://www.python.org")

