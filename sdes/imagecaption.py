#-*- coding: utf-8 -*-
import time 
import requests
import cv2
import operator
import numpy as np
import os
from google.cloud import translate
from sdes.glabel import GLABEL

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
translate_client = translate.Client()
target = 'vi'


_region = 'southeastasia'
_url = 'https://{}.api.cognitive.microsoft.com/vision/v1.0/analyze'.format(_region)
_key = 'them key o day'
_maxNumRetries = 10

def processRequest( json, data, headers, params ):

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json() ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json() ) )

        break
        
    return result
def CAPTION():
        pathToFileInDisk = r'image.jpg'
        with open( pathToFileInDisk, 'rb' ) as f:
            data = f.read()
        params = { 'visualFeatures' : 'description'} 

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = _key
        headers['Content-Type'] = 'application/octet-stream'

        json = None

        result = processRequest( json, data, headers, params )

        if result is not None:
            print(result)
            try:
                text=result["description"]["captions"][0]["text"]
                translation = translate_client.translate(
                    text,
                    target_language=target)
                text=format(translation['translatedText'])
                text=text.replace("một đóng lên","cận cảnh")
                return (text)
            except:
                return(GLABEL())
#print(CAPTION())

