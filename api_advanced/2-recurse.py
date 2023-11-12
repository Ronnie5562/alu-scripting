#!/usr/bin/python3
"""fetches the title of all hot posts for a given subreddit recursively"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Main function"""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.35.0"}
    PARAMS = {"after": after, "limit": 100}
    try:
        RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS,
                                allow_redirects=False)
        after = RESPONSE.json().get("data").get("after")
        HOT_POSTS = RESPONSE.json().get("data").get("children")
        [hot_list.append(post.get('data').get('title')) for post in HOT_POSTS]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
