#!/usr/bin/python3
"""
A script that fetches the value of the X-Request-ID from a URL response header
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-ID')

    print(request_id)
