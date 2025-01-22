#!/usr/bin/python3
"""
A module to sends a request to the URL and displays the X-Request-Id

Usage:
    python3 script_name.py <url>
Arguments:
    <url> (str): The URL to which the GET request will be sent.

Returns:
    None: The script prints the 'X-Request-ID' header to the console.
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    with opener.open(url) as response:
        # Get the value of the X-Request-ID from the header
        request_id = response.headers.get('X-Request-ID')

    if request_id is None:
        print("X-Request-ID: Not found")
    else:
        print(f"{request_id}\n")
