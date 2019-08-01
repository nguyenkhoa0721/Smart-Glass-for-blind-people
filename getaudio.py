import requests
import json
import urllib
url = "https://asr2.openfpt.vn/tts/callback"
def GA(text,title):
	headers = {
	    'content-type': "application/x-www-form-urlencoded",
	    'format': "mp3",
	    'prosody': "1",
	    'speed': "0",
	    'voice': "hatieumai"
	    }
	body=text
	body=body.encode('utf-8')
	r = requests.post(url, headers=headers,data=body, verify=False)
	urll=(r.json()['url'])
	req = requests.get(urll, stream=True, verify=False)
	req.raise_for_status()
	with open('./TTSlib/'+title+'.mp3', 'wb') as fd:
	    for chunk in req.iter_content(chunk_size=50000):
	        print('Received a Chunk')
	        fd.write(chunk)