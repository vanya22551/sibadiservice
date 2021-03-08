from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import News, Group
from.forms import NewsAddForm
import requests
import json

TOKEN = '8cc1afc194442efb656ec52ea0730268ca36bed1bc03e8dcb7338dcc8b6a727485c2e5d1425903854190d'
group_id_sib   = '-154434845' #Сибади 
group_id_omgtu = '-71122446'     #Oмгту
group_id_test = '-203090991'  #test
group_id_omgups = '-50875287' #ОМГУПС
group_id_omgu = '-58265344' #Омгу
group_id_omgpu = '-2944428' #Омгпу

def request_get(group):
	http_url = "https://api.vk.com/method/wall.get"
	group_id = group
	offset = 0
	count = 1

	r = requests.get(http_url,
		params={
		'v'           : '5.52',
		'owner_id'    : group_id,
		'count'       : count,
		'offset'      : offset,
		'access_token': TOKEN
		})

	
	json_str = r.json()

	return json_str



def get_text(json_string):

	text = json_string['response']['items'][0]['text']
	return text


def get_photo(json_string):

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
    else:
        photo = ''
        return photo

def face_page(request):
    return render(request, 'boTtelegramm/face_page.html')
      

def sibadi(request):
    json_string = request_get(group_id_sib)
 
    nws = News.objects.filter(group=1)
    news = []
    for i in nws:
        news.append(i)
    group = Group.objects.filter(group='sibadi')
    
    new = News.objects.filter(text=get_text(json_string=json_string))
    
    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        p = get_photo(json_string=json_string)
        file = form.save(commit=False)
        file.text = txt
        file.photo = p
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/sibadi.html', context)


def omgtu(request):

    json_string = request_get(group_id_omgtu)
    
    nws = News.objects.filter(group=2)
    news = []
    for i in nws:
        news.append(i)
    
    group = Group.objects.filter(group='omgtu')

    new = News.objects.filter(text=get_text(json_string=json_string))

    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        p = get_photo(json_string=json_string)
        file = form.save(commit=False)
        file.text = txt
        file.photo = p
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/Omgtu.html', context)


def omgups(request):

    json_string = request_get(group_id_omgups)
    nws = News.objects.filter(group=3)
    news = []
    for i in nws:
        news.append(i)
    group = Group.objects.filter(group='omgups')

    new = News.objects.filter(text=get_text(json_string=json_string))

    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        p = get_photo(json_string=json_string)
        file = form.save(commit=False)
        file.text = txt
        file.photo = p
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/Omgups.html', context)


def omgu(request):

    json_string = request_get(group_id_omgu)
    nws = News.objects.filter(group=4)
    news = []
    for i in nws:
        news.append(i)
    group = Group.objects.filter(group='omgu')

    new = News.objects.filter(text=get_text(json_string=json_string))

    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        p = get_photo(json_string=json_string)
        file = form.save(commit=False)
        file.text = txt
        file.photo = p
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/Omgu.html', context)


def omgpu(request):

    json_string = request_get(group_id_omgpu)
    nws = News.objects.filter(group=5)
    news = []
    for i in nws:
        news.append(i)
    group = Group.objects.filter(group='omgpu')

    new = News.objects.filter(text=get_text(json_string=json_string))

    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        p = get_photo(json_string=json_string)
        file = form.save(commit=False)
        file.text = txt
        file.photo = p
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/Omgpu.html', context)


def test(request):

    json_string = request_get(group_id_test)
    nws = News.objects.filter(group=6)
    news = []
    for i in nws:
        news.append(i)

    print(news)
    group = Group.objects.filter(group='test')
    news.reverse()
    print(news)
    new = News.objects.filter(text=get_text(json_string=json_string))

    if not new:
        form = NewsAddForm()
        txt = get_text(json_string=json_string)
        file = form.save(commit=False)
        try:
            p = get_photo(json_string=json_string)
            file.photo = p
        except:
            'yt'
        file.text = txt
        file.group = group[0]
        file.save() 


    for new in news:
        print(new.Date)
    context = {
        'news': news
    }
    return render(request, 'boTtelegramm/test.html', context)




