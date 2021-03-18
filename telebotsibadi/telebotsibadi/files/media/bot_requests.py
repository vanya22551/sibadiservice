import requests
import json
import time
import os
from config import TOKEN
"""
def write_json(data):
	with open('posts.json', 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)
"""  
def get_posts(count):
	http_url   = "https://api.vk.com/method/wall.get"
	group_id   = '-154434845'
	offset     = 0
	post_text  = []
	src_posts  = []
	type_media = []

	r = requests.get(http_url,
		params={
		'v'           : '5.52',
		'owner_id'    : group_id,
		'count'       : count,
		'offset'      : offset,
		'access_token': TOKEN
		})

	#write_json(r.json())

	json_string = r.json()
	
	for i in range(count):
		if json_string['response']['items'][i]['id'] == 2214:
			post_text.append('Из-за этого поста с репостом у меня сломалась прога, а также компьютер, жизнь, умерла собака, взорвался телефон и вообще, всё стало очень плохо о_О')
		else:
			post_text.append(json_string['response']['items'][i]['text'])

	for i in range(count):
		if json_string['response']['items'][i]['id'] == 2214:
			type_media.append(0)
		else:
			type_media.append(json_string['response']['items'][i]['attachments'][0]['type'])
	
	for i in range(len(type_media)):
		if type_media[i] == 'album':
			src_posts.append(json_string['response']['items'][i]['attachments'][0][type_media[i]]['thumb']['photo_1280'])
		elif type_media[i] == 'photo':
			src_posts.append(json_string['response']['items'][i]['attachments'][0][type_media[i]]['photo_1280'])
		elif type_media[i] == 'link':
			src_posts.append(json_string['response']['items'][i]['attachments'][0][type_media[i]]['photo']['photo_604'])
		elif type_media[i] == 'video':
			src_posts.append(json_string['response']['items'][i]['attachments'][0][type_media[i]]['photo_1280'])
		elif json_string['response']['items'][i]['id'] == 2214:
			src_posts.append('https://static10.tgstat.ru/channels/_0/d3/d3cabf58f9fccb8543e36ca816874d7d.jpg')

def main():
	get_posts(10)

if __name__ == "__main__":
	main()