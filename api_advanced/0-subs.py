#!/usr/bin/python3
"""0-subs.py"""

import requests


def number_of_subscribers(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")
    except Exception as e:
        return 0
