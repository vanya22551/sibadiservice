import requests
import json

TOKEN = '65581361481e9abf8f1a0164751cf05b94a06740313ec772c78aae01aaa33b3ea80c9f7ac7ea58d2d4ee4'


def write_json(data):
	with open('posts.json', 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)

def request_get():
	http_url   = "https://api.vk.com/method/wall.get"
	group_id   = '-154434845'
	#group_id = '-71122446'
	#group_id = '-203090991'
	offset     = 0
	count = 1

	r = requests.get(http_url,
		params={
		'v'           : '5.52',
		'owner_id'    : group_id,
		'count'       : count,
		'offset'      : offset,
		'access_token': TOKEN
		})

	write_json(r.json())
	json_string = r.json()

	return json_string
"""
def checkPinned(json_string):
	if json_string['response']['items'][0]['is_pinned']:
		return 1
	elif json_string['response']['items'][0]['is_pinned'] == None:
		return 0
"""
def get_text(json_string):
#	if checkPinned(request_get()):
	text = json_string['response']['items'][0]['text']
	return text
	#else:
	#	return json_string['response']['items'][0]['text']

def get_photo(json_string):
	"""
	if checkPinned(request_get()):

		type_media = json_string['response']['items'][1]['attachments'][0]['type']

		if type_media == 'album':
			return json_string['response']['items'][1]['attachments'][0][type_media]['thumb']['photo_604']
		elif type_media == 'photo':
			return json_string['response']['items'][1]['attachments'][0][type_media]['photo_604']
		elif type_media == 'link':
			return json_string['response']['items'][1]['attachments'][0][type_media]['photo']['photo_604']
		elif type_media == 'video':
			return json_string['response']['items'][1]['attachments'][0][type_media]['photo_800']
		elif json_string['response']['items'][1]['id'] == 2214:
			return 'https://static10.tgstat.ru/channels/_0/d3/d3cabf58f9fccb8543e36ca816874d7d.jpg'
	else:
		"""
	type_media = json_string['response']['items'][0]['attachments'][0]['type']

	if type_media == 'album':
		photo = json_string['response']['items'][0]['attachments'][0][type_media]['thumb']['photo_604'] 
		return photo
	elif type_media == 'photo':
		photo = json_string['response']['items'][0]['attachments'][0][type_media]['photo_604']
		return photo
	elif type_media == 'link':
		photo = json_string['response']['items'][0]['attachments'][0][type_media]['photo']['photo_604']
		return photo
	elif type_media == 'video':
		photo = json_string['response']['items'][0]['attachments'][0][type_media]['photo_800']
		return photo
print(get_text(request_get()))
print(get_photo(request_get()))