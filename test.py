from TwitterAPI import TwitterAPI
import json
from pprint import pprint
import json, ast

consumer_key = 'SoPaOn5tDkIkHtUT5kI2jMFMy'
consumer_secret = 'g3eEMpKX0lUXM2Ysly43Io432pVCFzODWkIakumoGFu9GzJ3V7'
access_token_key = '717264875844542464-faFh7QCa2lgHISQT6TEh0465XqvOcIS'
access_token_secret = 'EKrbkUkuIJPvP4v4YJaKLJYJCFYx1NhAVEEn87xUyUk5s'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = {}

r = api.request('search/tweets', {'q':'#carnival', 'filter':'images'})
for item in r:
	print item
