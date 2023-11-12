#!/usr/bin/python3
"""Doc"""
import requests


def count_words(subreddit, word_list, after="", words_count={}):
    """"Doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100" \
        .format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    res = requests.get(url, headers=header, params=param)

    if res.status_code != 200:
        return

    json_res = res.json()  # chch
    after = json_res.get('data').get('after')
    has_next = after is not None
    hot_titles = []
    words = [word.lower() for word in word_list]

    if len(words_count) == 0:
        words_count = {word: 0 for word in words}
    # print(words_count)
    hot_articles = json_res.get('data').get('children')
    [hot_titles.append(article.get('data').get('title'))
     for article in hot_articles]

    # loop through all titles
    for i in range(len(hot_titles)):
        # make the title as a list of word
        # title_words = hot_titles[i].lower().split()
        for title_word in hot_titles[i].lower().split():
            for word in words:
                if word.lower() == title_word:
                    words_count[word] = words_count.get(word) + 1
                # else:
                #     # pass
                #     print(word.lower() + " != " + title_word)

    if has_next:
        # print(after + "\t" + str(has_next))
        return count_words(subreddit, word_list, after, words_count)
    else:

        words_count = dict(filter(lambda item: item[1] != 0,
                                  words_count.items()))
        # their python version is not making people’s life easier
        # words_count = {key: value for key, value in
        #                sorted(words_count.items(),
        #                       key=lambda item: item[1], reverse=True)}

        words_count = sorted(words_count.items(),
                             key=lambda item: item[1],
                             reverse=True)

        for i in range(len(words_count)):
            print("{}: {}".format(words_count[i][0],
                                  words_count[i][1]))
