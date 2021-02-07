from django.shortcuts import render
from django.http import HttpResponse
import ipinfo
import requests
# Create your views here.
apikey = ["55f7d6b91d8445b9be9fa8599e30a932","227d497ed1e44439b2d709f21dddf5f5"]
ipinfo_token = "7d5765cb4b4bc8"
weathermap = "04627a171de78262fa1dc9b42ec992e8"

def index(request):
    
    countries = "in"
    apikey = "55f7d6b91d8445b9be9fa8599e30a932"
    
    url = f"https://newsapi.org/v2/top-headlines?country={countries}&apiKey={apikey}"
    news = requests.get(url)
    news_formatted =  news.json()
    ip = request.META['REMOTE_ADDR']
    print(ip)
    print(news_formatted["totalResults"])
    return render(request,'index.html',{"news_list":news_formatted["articles"],"name":"IN","countryName":"in"})


def countrySpecific(request,name):

    countriesDic = {
        'ar':'argentina',
        'au':'australia',
        'at':'austria',
        'be':'belgium',
        'br':'brazil',
        'bg':'bulgaria',
        'ca':'canada',
        'cn':'china',
        'co':'colombia',
        'cu':'cuba',
        'cz':'czech republic',
        'eg':'egypt',
        'fr':'france',
        'de':'germany',
        'gr':'greece',
        'hk':'hong kong',
        'hu':'hungary',
        'in':'india',
        'id':'indonesia',
        'ie':'ireland',
        'il':'israel',
        'it':'italy',
        'jp':'japan',
        'lv':'latvia',
        'lt':'lithuania',
        'my':'malaysia',
        'mx':'mexico',
        'ma':'morocco',
        'nl':'netherlands',
        'nz':'new zealand',
        'ng':'nigeria',
        'no':'norway',
        'ph':'phillippines',
        'pl':'poland',
        'pt':'portugal',
        'ro':'romania',
        'ru':'russia',
        'sa':'saudi arabia',
        'rs':'serbia',
        'sg':'singapore',
        'sk':'slovakia',
        'si':'slovenia',
        'za':'south africa',
        'kr':'south korea',
        'se':'sweden',
        'ch':'switzerland',
        'tw':'taiwan',
        'th':'thailand',
        'tr':'turkey',
        'ae':'uea',
        'ua':'ukraine',
        'us':'united states',
        'gb':'united kingdom',
        've':'venuzuela'
    }

    countries = name
    apikey = "55f7d6b91d8445b9be9fa8599e30a932"
    pageNum = 1
    print(request.POST.get("but"))
    if(request.method == "POST"):
        pageNum = int(request.POST.get("but"))

    url = f"https://newsapi.org/v2/top-headlines?country={countries}&pageSize=20&page={pageNum}&apiKey={apikey}"
    news = requests.get(url)
    news_formatted =  news.json()


    return render(request,'index.html',{"news_list":news_formatted["articles"],"name":countriesDic[f"{name}"],"pageNum":pageNum,"countryName":name})


def countryCategory(request,name,category):
    
    countriesDic = {
        'ar':'argentina',
        'au':'australia',
        'at':'austria',
        'be':'belgium',
        'br':'brazil',
        'bg':'bulgaria',
        'ca':'canada',
        'cn':'china',
        'co':'colombia',
        'cu':'cuba',
        'cz':'czech republic',
        'eg':'egypt',
        'fr':'france',
        'de':'germany',
        'gr':'greece',
        'hk':'hong kong',
        'hu':'hungary',
        'in':'india',
        'id':'indonesia',
        'ie':'ireland',
        'il':'israel',
        'it':'italy',
        'jp':'japan',
        'lv':'latvia',
        'lt':'lithuania',
        'my':'malaysia',
        'mx':'mexico',
        'ma':'morocco',
        'nl':'netherlands',
        'nz':'new zealand',
        'ng':'nigeria',
        'no':'norway',
        'ph':'phillippines',
        'pl':'poland',
        'pt':'portugal',
        'ro':'romania',
        'ru':'russia',
        'sa':'saudi arabia',
        'rs':'serbia',
        'sg':'singapore',
        'sk':'slovakia',
        'si':'slovenia',
        'za':'south africa',
        'kr':'south korea',
        'se':'sweden',
        'ch':'switzerland',
        'tw':'taiwan',
        'th':'thailand',
        'tr':'turkey',
        'ae':'uea',
        'ua':'ukraine',
        'us':'united states',
        'gb':'united kingdom',
        've':'venuzuela'
    }

    countries = name
    apikey = "55f7d6b91d8445b9be9fa8599e30a932"
    pageNum = 1
    
    if(request.method == "POST"):
        pageNum = int(request.POST.get("but"))

    url = f"https://newsapi.org/v2/top-headlines?country={countries}&category={category}&pageSize=20&page={pageNum}&apiKey={apikey}"
    news = requests.get(url)
    news_formatted =  news.json()


    return render(request,'index.html',{"news_list":news_formatted["articles"],"name":countriesDic[f"{name}"],"pageNum":pageNum,"countryName":name,'category':category})


def topic(request):

    countriesDic = {
        'ar':'argentina',
        'au':'australia',
        'at':'austria',
        'be':'belgium',
        'br':'brazil',
        'bg':'bulgaria',
        'ca':'canada',
        'cn':'china',
        'co':'colombia',
        'cu':'cuba',
        'cz':'czech republic',
        'eg':'egypt',
        'fr':'france',
        'de':'germany',
        'gr':'greece',
        'hk':'hong kong',
        'hu':'hungary',
        'in':'india',
        'id':'indonesia',
        'ie':'ireland',
        'il':'israel',
        'it':'italy',
        'jp':'japan',
        'lv':'latvia',
        'lt':'lithuania',
        'my':'malaysia',
        'mx':'mexico',
        'ma':'morocco',
        'nl':'netherlands',
        'nz':'new zealand',
        'ng':'nigeria',
        'no':'norway',
        'ph':'phillippines',
        'pl':'poland',
        'pt':'portugal',
        'ro':'romania',
        'ru':'russia',
        'sa':'saudi arabia',
        'rs':'serbia',
        'sg':'singapore',
        'sk':'slovakia',
        'si':'slovenia',
        'za':'south africa',
        'kr':'south korea',
        'se':'sweden',
        'ch':'switzerland',
        'tw':'taiwan',
        'th':'thailand',
        'tr':'turkey',
        'ae':'uea',
        'ua':'ukraine',
        'us':'united states',
        'gb':'united kingdom',
        've':'venuzuela'
    }
    name="india"
    topicinput = "covid-19"
    apikey = "55f7d6b91d8445b9be9fa8599e30a932"
    pagenumber = 1
    
    if(request.method == "POST"):
        topicinput = request.POST.get("topicinput")
        if(request.POST.get("pagenum")):
            pagenumber = int(request.POST.get("pagenum"))

    url = f"https://newsapi.org/v2/everything?q={topicinput}&pageSize=50&page={pagenumber}&apiKey={apikey}"
    news = requests.get(url)
    news_formatted =  news.json()


    return render(request,'topic.html',{"news_list":news_formatted["articles"],"topicname":topicinput,"pagenumber":pagenumber,"name":name})


def home(request):

    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    countriesDic = {
        'in':'india',
        'us':'USA',
        'gb':'united kingdom',
        'au':'australia',
        'ca':'canada',
        'nz':'new zealand',
        'sa':'saudi arabia'
        
        }

    handler = ipinfo.getHandler(ipinfo_token)
    ip = get_client_ip(request)
    
    details = handler.getDetails(ip)
    loc = details.city
    reg = details.region
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={loc}&units=metric&appid={weathermap}")
    weather_json = weather.json()
    resultsdic = []
    for x in countriesDic:
        
        news = requests.get(f"https://newsapi.org/v2/top-headlines?country={x}&pageSize=10&apiKey={apikey[0]}")
        news_list = news.json()
        if(news_list['status'] != "ok"):
            news = requests.get(f"https://newsapi.org/v2/top-headlines?country={x}&pageSize=10&apiKey={apikey[1]}")
            news_list = news.json()
        news_list["country"] = countriesDic[x]
        news_list["countryCode"] = x
        resultsdic.append(news_list)

    
    

    
    return render(request,'test.html',{"news_list":news_list,"countryList":countriesDic,"resultsdic":resultsdic,"weather":weather_json,"loc":loc,"reg":reg})