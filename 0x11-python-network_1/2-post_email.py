#!/usr/bin/python3
"""Python script"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    post_dict = {"email": sys.argv[2]}
    url_encoded_data = urllib.parse.urlencode(post_dict)
    post_data = url_encoded_data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data=post_data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
