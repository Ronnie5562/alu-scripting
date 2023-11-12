#!/usr/bin/python3
"""fetches the title of all hot posts for a given subreddit recursively"""

import requests


def count_words(subreddit, word_list=[], hot_list=[], after=""):
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
            return count_words(subreddit, hot_list=hot_list, after=after)
        
        new_dict = {}
        word_list = set(word_list)
        for title in hot_list:
            for word in title:
                if word.lower() in new_dict:
                    new_dict[word.lower()] += 1
                else:
                    new_dict.update({word.lower(): 1})
        
        for key, value in sorted(new_dict):
            if (key in word_list) and (value > 0):
                print(f"{key}: {value}")
        
    except Exception:
        return None
