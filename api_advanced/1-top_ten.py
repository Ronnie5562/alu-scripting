#!/usr/bin/python3
import requests
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

def top_ten(subreddit):
    """Main function"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        """_summary_
        """
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [print(post.get('data').get('title')) for post in HOT_POSTS]
    except Exception as e:
        """_summary_
        """
        print(None)