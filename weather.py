# -*- coding: utf8 -*-
import re
import sys
import requests
#xu ly tieng viet 
patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}
def convert(text):
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

def WEATHER(text):
    text=convert(text)
    #get link
    r = requests.get('http://api.openweathermap.org/data/2.5/find?q='+text+
                     '&type=like'+
                     '&mode=json'+
                     '&lang=vi'+
                     '&units=metric'+
                     '&appid=2c31e94cea3ba552d2795e9c1fb7dcb3')
    #phan tich
    info=r.json()
    temp=str(int(info["list"][0]["main"]["temp"]))
    humidity=str(float(info["list"][0]["main"]["humidity"]))
    humidity=humidity.replace('.', ' phẩy ')
    wind=str(float(info["list"][0]["wind"]["speed"]))
    wind=wind.replace('.', ' phẩy ')
    weather=str(info['list'][0]['weather'][0]['description'])
    #tao doan text
    text=weather+", nhiệt độ: "+temp+" độ xê, độ ẩm: "+humidity+" phần trăm, Gió: "+wind+" mét trên giây"
    return text
      
