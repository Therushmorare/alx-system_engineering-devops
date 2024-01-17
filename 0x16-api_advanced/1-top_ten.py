#!/usr/bin/python3
"""
Task 1
"""
import requests


def top_ten(subreddit):
    posts = ""
    if (type(subreddit) != str):
        posts = "None\n"
    else:
        api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'safari:alx/0.1.0'}
        response = requests.get(api_url, headers=headers)
        if response.status_code != 200:
            posts = "None\n"
        else:
            posts_json = response.json().get("data").get("children")
            for i in range(10):
                post_title = posts_json[i].get("data").get("title")
                posts += "{}\n".format(post_title)
    print(posts, end="")
