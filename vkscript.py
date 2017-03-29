import pprint
from urllib.parse import urlencode
import matplotlib.pyplot as plt
import networkx as nx
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
#
# params = {
#     'access_token': '',
#     'v': VERSION
# }
#
