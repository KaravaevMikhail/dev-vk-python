import requests
import json

f = open('token.txt', 'r')
token = f.read()
f.close()

r = requests.get('https://api.vk.com/method/friends.getOnline?user_id=266523857&v=5.52&access_token=' + token)
friends = json.loads(r.content)
frionl = friends['response']
print('Друзей онлайн:', len(frionl))