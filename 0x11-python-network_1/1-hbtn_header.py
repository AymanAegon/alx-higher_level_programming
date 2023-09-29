#!/usr/bin/python3
"""Python script"""
import urllib.request, sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
