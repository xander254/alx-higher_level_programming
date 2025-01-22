#!/usr/bin/python3
"""
A module to sends a request to the URL and displays the X-Request-Id

Usage:
    python3 script_name.py <url>
"""


import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-ID')

print(f"{request_id}\n")
