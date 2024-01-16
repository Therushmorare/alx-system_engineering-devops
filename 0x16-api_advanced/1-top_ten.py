#!/usr/bin/python3

"""
Task 1
"""

import requests

def top_ten(subreddit):
        """ get top 10 posts """
        api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'safari:holberton/0.1.0'}
        response = requests.get(api_url, headers=headers)

        posts = ""
        if (type(subreddit) != str):
            posts = "None\n"

        if response.status_code != 200:
            posts = "None\n"
        else:
            posts_json = response.json().get("data").get("children")
            for i in range(10):
                post_title = posts_json[i].get("data").get("title")
                posts += "{}\n".format(post_title)

        return (print(posts, end=""))
