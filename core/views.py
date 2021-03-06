from django.shortcuts import render
import requests
from django.contrib import messages
import publicip
from googleapiclient.discovery import build




def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7d3e88675b678961df9ba90435e7a5f6'
    
    if request.method == 'POST':
        searchWord = request.POST.get('search','')
        try:        
            city = searchWord
            r = requests.get(url.format(city)).json()
            weather = {
        
        'city':city,
        'temperature':r['main']['temp'],
        'wind':r['wind']['speed'],
        'wind_deg':r['wind']['deg'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
             } 
            context = {
        'weather':weather,
            }
            return render(request,'core/index.html',context)
        except :
            messages.error(request, 'city not found !!')

    city = 'jijel'
    r = requests.get(url.format(city)).json()
    weather = {
        'city':city,
        'temperature':r['main']['temp'],
        'wind':r['wind']['speed'],
        'wind_deg':r['wind']['deg'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
             } 
    context = {
        'weather':weather,
            }
    return render(request,'core/index.html',context)



def ip(request):

    ip = requests.get('http://ipinfo.io/json').json()['ip']
    url = "http://api.ipstack.com/{}?access_key=36b65ab092455a14f25413ae9dc8e9b0"
    if request.method == 'POST':
        searchWord = request.POST.get('search','')
        try:        
            ip = searchWord

            r = requests.get(url.format(ip)).json()
            context = {
        'ip':ip,
        'continent_name':r['continent_name'],
        'country_name':r['country_name'],
        'country_flag':r['location']['country_flag'],
        'capital':r['location']['capital'],
        'languages':r['location']['languages'][0]['name'],
        'region_name':r['region_name'],
        'region_code':r['region_code'],
        'city':r['city'],
        'zip':r['zip'],
        'latitude':r['latitude'],
        'longitude':r['longitude'],
            }
            return render(request,'core/ip.html',context)
        except :
            messages.error(request, 'IP not found !!')
    ip = requests.get('http://ipinfo.io/json').json()['ip']
    r = requests.get(url.format(ip)).json()
    context = {
        'ip':ip,
        'continent_name':r['continent_name'],
        'country_name':r['country_name'],
        'country_flag':r['location']['country_flag'],
        'capital':r['location']['capital'],
        'languages':r['location']['languages'][0]['name'],
        'region_name':r['region_name'],
        'region_code':r['region_code'],
        'city':r['city'],
        'zip':r['zip'],
        'latitude':r['latitude'],
        'longitude':r['longitude'],


            }

    return render(request,'core/ip.html',context)


def news(request):

    url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c9e0bed47e6b44dca5a613fc39accd7d')
    r = requests.get(url).json()

    article0 = {
    'title':r['articles'][0]['title'],
    'description':r['articles'][0]['description'],
    'url':r['articles'][0]['url'],
    'urlToImage':r['articles'][0]['urlToImage'],
    'publishedAt':r['articles'][0]['publishedAt'],
    'author':r['articles'][0]['author'],}

    article1 = {
    'title':r['articles'][1]['title'],
    'description':r['articles'][1]['description'],
    'url':r['articles'][1]['url'],
    'urlToImage':r['articles'][1]['urlToImage'],
    'publishedAt':r['articles'][1]['publishedAt'],
    'author':r['articles'][1]['author'],}

    article2 = {
    'title':r['articles'][2]['title'],
    'description':r['articles'][2]['description'],
    'url':r['articles'][2]['url'],
    'urlToImage':r['articles'][2]['urlToImage'],
    'publishedAt':r['articles'][2]['publishedAt'],
    'author':r['articles'][2]['author'],}
    
    article3 = {
    'title':r['articles'][3]['title'],
    'description':r['articles'][3]['description'],
    'url':r['articles'][3]['url'],
    'urlToImage':r['articles'][3]['urlToImage'],
    'publishedAt':r['articles'][3]['publishedAt'],
    'author':r['articles'][3]['author'],}

    article4 ={
    'title':r['articles'][4]['title'],
    'url':r['articles'][4]['url'],}

    article5 = {
    'title':r['articles'][5]['title'],
    'url':r['articles'][5]['url'],}

    article6 = {
    'title':r['articles'][6]['title'],
    'url':r['articles'][6]['url'],}

    article7 = {
    'title':r['articles'][7]['title'],
    'url':r['articles'][7]['url'],}

    article8 = {
    'title':r['articles'][8]['title'],
    'url':r['articles'][8]['url'],
    'urlToImage':r['articles'][8]['urlToImage'],
}
    article9 = {
    'title':r['articles'][9]['title'],
    'url':r['articles'][9]['url'],
    'urlToImage':r['articles'][9]['urlToImage'],
}
    article10 = {
    'title':r['articles'][10]['title'],
    'url':r['articles'][10]['url'],
    'urlToImage':r['articles'][10]['urlToImage'],
}
    article11 = {
    'title':r['articles'][11]['title'],
    'url':r['articles'][11]['url'],
    'urlToImage':r['articles'][11]['urlToImage'],
}
    article12 = {
    'title':r['articles'][12]['title'],
    'url':r['articles'][12]['url'],
    'urlToImage':r['articles'][12]['urlToImage'],
}
    article13 = {
    'title':r['articles'][13]['title'],
    'url':r['articles'][13]['url'],
    'urlToImage':r['articles'][13]['urlToImage'],
}
    article14 = {
    'title':r['articles'][14]['title'],
    'url':r['articles'][14]['url'],
    'urlToImage':r['articles'][14]['urlToImage'],
}
    article15 = {
    'title':r['articles'][15]['title'],
    'url':r['articles'][15]['url'],
    'urlToImage':r['articles'][15]['urlToImage'],
}
    article16 = {
    'title':r['articles'][16]['title'],
    'url':r['articles'][16]['url'],}

    article17 = {
    'title':r['articles'][17]['title'],
    'url':r['articles'][17]['url'],}

    article18 = {
    'title':r['articles'][18]['title'],
    'url':r['articles'][18]['url'],}

    article19 = {
    'title':r['articles'][19]['title'],
    'url':r['articles'][19]['url'],}



    context = {
    'article0':article0,'article1':article1,
    'article2':article2, 'article3':article3,
    'article4':article4, 'article5':article5,'article6':article6, 'article7':article7,
    'article8':article8,'article9':article9,'article10':article10,'article11':article11,
    'article12':article12,'article13':article13,'article14':article14,'article15':article15,
    'article16':article16,'article17':article17,'article18':article18,
    'article19':article19,
        }

    return render(request,'core/news.html',context)


def youtube(request):
    searchWord = 'Algerian viral video'
    if request.method == 'POST':
        searchWord = request.POST.get('search','')
    else:
        pass
    
    api_key = 'AIzaSyCb5VnUNMp9XEKB0T5FRErO0xl_Xr7xIS4'
    youtube = build('youtube','v3',developerKey=api_key)
    r = youtube.search().list(q=searchWord,maxResults=9,part='snippet',type='video')
    res = r.execute()
    
    
    video0 = {
        'title':res['items'][0]['snippet']['title'],
        'id':res['items'][0]['id']['videoId'],
        'image':res['items'][0]['snippet']['thumbnails']['high']['url'],
        'description':res['items'][0]['snippet']['description'],
        'publishedAt':res['items'][0]['snippet']['publishedAt'],
    }
    video1 = {
        'title':res['items'][1]['snippet']['title'],
        'id':res['items'][1]['id']['videoId'],
        'image':res['items'][1]['snippet']['thumbnails']['high']['url'],
        'description':res['items'][1]['snippet']['description'],
        'publishedAt':res['items'][1]['snippet']['publishedAt'],
    }
    video2 = {
        'title':res['items'][2]['snippet']['title'],
        'id':res['items'][2]['id']['videoId'],
        'image':res['items'][2]['snippet']['thumbnails']['high']['url'],
        'description':res['items'][2]['snippet']['description'],
        'publishedAt':res['items'][2]['snippet']['publishedAt'],
    }

    video3 = {
        'title':res['items'][3]['snippet']['title'],
        'id':res['items'][3]['id']['videoId'],
        'image':res['items'][3]['snippet']['thumbnails']['high']['url'],
    }
    video4 = {
        'title':res['items'][4]['snippet']['title'],
        'id':res['items'][4]['id']['videoId'],
        'image':res['items'][4]['snippet']['thumbnails']['high']['url'],
    }
    video5 = {
        'title':res['items'][5]['snippet']['title'],
        'id':res['items'][5]['id']['videoId'],
        'image':res['items'][5]['snippet']['thumbnails']['high']['url'],
    }
    video6 = {
        'title':res['items'][6]['snippet']['title'],
        'id':res['items'][6]['id']['videoId'],
        'image':res['items'][6]['snippet']['thumbnails']['high']['url'],
    }
    video7 = {
        'title':res['items'][7]['snippet']['title'],
        'id':res['items'][7]['id']['videoId'],
        'image':res['items'][7]['snippet']['thumbnails']['high']['url'],
    } 
    video8 = {
        'title':res['items'][8]['snippet']['title'],
        'id':res['items'][8]['id']['videoId'],
        'image':res['items'][8]['snippet']['thumbnails']['high']['url'],
    }     



    context = {
        'video0':video0,'video1':video1,'video2':video2,
        'video3':video3,'video4':video4,'video5':video5,
        'video6':video6,'video7':video7,'video8':video8,

    }
    return render(request, 'core/youtube.html', context)