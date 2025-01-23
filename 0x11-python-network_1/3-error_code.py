#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            html = html.decode('utf-8')
            print(html)

    except urllib.HTTPError as e:
        print(f"Error code: {e.code}")
