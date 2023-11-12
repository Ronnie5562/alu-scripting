#!/usr/bin/python3
'''a recursive function that queries the Reddit API,
 parses the title of all hot articles, and prints a
 sorted count of given keywords
'''
import requests


def count_words(subreddit, word_list, fullname="", count=0, hash_table={}):
    '''fetches all hot posts in a subreddit
    Return:
        None - if subreddit is invalid
    '''
    if subreddit is None or not isinstance(subreddit, str) or \
       word_list is None or word_list == []:
        return
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': fullname, 'count': count}
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    info = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)
    if info.status_code != 200:
        return None
    info_json = info.json()
    results = info_json.get('data').get('children')
    new_packet = [post.get('data').get('title') for post in results]
    for title in new_packet:
        for word in word_list:
            word = word.lower()
            formatted_title = title.lower().split(" ")
            if word in formatted_title:
                if (word in hash_table.keys()):
                    hash_table[word] += formatted_title.count(word)
                else:
                    hash_table[word] = formatted_title.count(word)
    after = info_json.get('data').get('after', None)
    dist = info_json.get('data').get('dist')
    count += dist
    if after:
        count_words(subreddit, word_list, after, count, hash_table)
    else:
        {print('{}: {}'.format(key, value)) for
         key, value in sorted(hash_table.items(), key=lambda i: (-i[1], i[0]))}
