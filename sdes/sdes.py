import cloudsight
from google.cloud import translate
import time 
import os

def SDES():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
    translate_client = translate.Client()
    target = 'vi'

    auth = cloudsight.SimpleAuth('nWzHSM1Kej9ftd5ld6u59A')
    api = cloudsight.API(auth)

    with open('image.jpg', 'rb') as f:
        response = api.image_request(f, 'image.jpg', {
            'image_request[locale]': 'en-US',
        })
    status = api.wait(response['token'], timeout=30)
    text=status['name']
    translation = translate_client.translate(
            text,
            target_language=target)
    text=format(translation['translatedText'])
    return(str(text))

