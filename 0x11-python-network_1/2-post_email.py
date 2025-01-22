#!/usr/bin/python3
"""
Make a post request
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    encoded_data = urllib.parse.urlencode(data).encode("utf-8")

    request = urllib.request.Request(url, data=encoded_data, method="POST")
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
    print(body)
