#!/usr/bin/python3
"""Python script"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(url)
    arr = req.json()
    c = 0
    for i in arr:
        if c >= 10:
            break
        sha = i["sha"]
        name = i["commit"]["author"]["name"]
        print(f"{sha}: {name}")
        c+=1
