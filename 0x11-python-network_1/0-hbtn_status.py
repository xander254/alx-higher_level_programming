#!/usr/bin/python3
""" A module to fetch and parse simple data from a URL using urllib """

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print(
    "Body response:\n"
    f"\t- type: {type(html)}\n"
    f"\t- content: {html}\n"
    f"\t- utf8 content: {html.decode('utf-8')}"
)
