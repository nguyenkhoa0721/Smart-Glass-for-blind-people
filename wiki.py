import wikipedia
import requests
wikipedia.set_lang("vi")
def xuly(text):
    text=text.lower()
    text=text.replace('+','')
    text=text.replace('/','')
    text=text.replace('*','')
    text=text.replace('-','')
    text=text.replace('.','')
    text=text.replace(',','')
    return text
def WIKI(text):
    check=False
    api='AIzaSyBR-JL9i1IjPF53DLjWBI6Vi_f0SvWbvO4'
    url=('https://kgsearch.googleapis.com/v1/entities:search?languages=vi&query='+
        text+
        '&fields=itemListElement&key='+api+'&limit=1')
    r = requests.get(url)
    gdata=(r.json())
    temp=str(gdata)
    if (temp.find('detailedDescription')!=-1):
        gname=gdata["itemListElement"][0]['result']['name']
        gans=gdata["itemListElement"][0]['result']['detailedDescription']['articleBody']
        gname=gdata["itemListElement"][0]['result']['name']
        check=True
        if (xuly(gname)==xuly(text)):
            return gans
    try:
        wans = wikipedia.summary(text,sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        data=e.options
        wans = wikipedia.summary(data[0],sentences=1)
    except wikipedia.exceptions.PageError as  e:
        if (check==False):
            return "Không có"
        else:
            return gans
    return wans

