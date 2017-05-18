import pprint
from urllib.parse import urlencode
import requests


AUTHORISE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.62'
APP_ID = 5954886


auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'response_type': 'token',
    'scope': 'friends,status,video',
    'v': VERSION
}

print('?'.join((AUTHORISE_URL, urlencode(auth_data))))


token_url = 'https://oauth.vk.com/authorize?client_id=5954886&display=mobile&response_type=token&scope=friends%2Cstatus%2Cvideo&v=5.62'

params = {
    'access_token': 'c0905f80c0e4ac7a0d37c5e225e92138c47da2ead1a7b809f004586ae1f7e8bdec0f1dc23be339b75948f',
    'v': VERSION
}

params['user_id'] = 13104328
params['fields'] = 'last_name'

response = requests.get('https://api.vk.com/method/friends.get', params)
my_friends = response.json()['response']['items']
pprint.pprint(my_friends)

def get_friends_vk(my_friends):
    overall_friends = []
    friend_data = dict()
    for friend in my_friends:
        try:
            overall_friends.append(friend)
            print('-'* 30)
            print('Друзья', friend['first_name'], friend['last_name'], friend['id'])
            friend_data['user_id'] = friend['id']
            params['user_id'] = friend['id']# друзья друга
            print(params)
            fr_of_friends = requests.get('https://api.vk.com/method/friends.get', params)
            overall_friends.extend(fr_of_friends.json()['response']['items'])
        except KeyError:
            continue
        except TypeError:
            continue
    return overall_friends

get_friends_vk(my_friends)




