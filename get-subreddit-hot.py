import requests
import pandas as pd

from reddit import headers

res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

for post in res.json()['data']['children']:
    print(post['data']['title'])


# make a request for the trending posts in /r/Python
res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)

df.head()