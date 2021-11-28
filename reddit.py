import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('50AL2O9RnxO5jE1KLzu6xw', 'XHLL5z-wY_OMd6GYYQNh_1VnMZSPkQ')
#
# # here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'sch1024',
        'password': 'Infr@red'}

# # setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}
#
# # send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
print(res)
# # convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']
print(TOKEN)
# # add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
resp = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
