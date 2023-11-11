#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Main function"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0