#!/usr/bin/python3
""" Function to count words in all hot post of the given Reddit_subreddit
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursive function that queries the Reddit API, 
    parses the title of all hot articles
    """
    if not word_list or word_list == [] or not subreddit:
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    headers = {'User-Agent': 'Mozilla/10.0/API'}
    
    params = {'limit': 100}
    
    if after:
        
        params['after'] = after
        
    response = requests.get(url,
                            headers=headers, 
                            params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    main_data = response.json()
    
    data = main_data.get('data')
    
    children = data.get('children')
    
    for post in  children:
        title = post.get(data, {}).get ('title').lower()
        
        for word in word_list:
            if word.lower() in title:
                
                count_words = count.get()