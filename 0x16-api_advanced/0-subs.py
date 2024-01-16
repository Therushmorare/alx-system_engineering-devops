#!/usr/bin/python3

"""
Number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """ Init """
    url_api = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)

    if (type(subreddit) !=  str):
        return(0)

    if response.status_code != 200:
        return (0)

    return(response.json().get("data").get("subscribers"))
