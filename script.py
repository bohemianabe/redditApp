import pandas as pd
import requests

with open('clientID.txt', 'r') as f:
    clientid = f.read()

with open('secretKey.txt', 'r') as f:
    secretKey= f.read()

CLIENT_ID =  clientid
SECRET_KEY = secretKey

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

with open('pw.txt', 'r') as f:
    pw = f.read()

data = {
    'grant_type': 'password',
    'username': 'soulstonetchalla',
    'password': pw
}

headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

# requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()

res = requests.get('https://oauth.reddit.com/r/technology/hot', headers=headers, params={'limit': '50'})

# init an empty data frame
df = pd.DataFrame()



# loop through the children data and append a numbered object with the data I want
for post in res.json()['data']['children']:
    number = 0
    df = df.append({  number: [{
        'id': post['kind'] + "_" + post['data']['id'],
        'title': post['data']['title'],
        'imgThumbnail': post['data']['thumbnail'],
        'url': post['data']['url'] 
        }] 
    }, ignore_index=True)
    

    number += 1


# df.to_csv(r'C:\Users\agarr\Desktop\code\redditApp\data.csv')
# df.to_json(r'C:\Users\agarr\Desktop\code\redditApp\tech_data.json')


print(df)




