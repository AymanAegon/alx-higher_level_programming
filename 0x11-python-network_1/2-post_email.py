#!/usr/bin/python3
"""Python script"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    post_dict = {"email": sys.argv[2]}
    url_encoded_data = urllib.parse.urlencode(post_dict)
    post_data = url_encoded_data.encode("utf-8")
    with urllib.request.urlopen(sys.argv[1], data=post_data) as response:
        print(f"Your email is: {response.getheader('email')}")
