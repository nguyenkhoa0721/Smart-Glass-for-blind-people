import requests
import io
import base64
import cv2
#from skimage.filters import threshold_local
def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content).decode()
def document_ocr(base64_image):
    url = "https://vision.googleapis.com/v1/images:annotate?key=them_key_o_day"
    header = {"Content-Type": "application/json"}
    body = {
        "requests":
        [{
            "image":
            {
                "content": base64_image,
            },
                   
            "features":
            [{
                "type": "DOCUMENT_TEXT_DETECTION",
                "maxResults": 1,
            }],
               
            "imageContext":
            {
                "languageHints": ['vi']
            },
        }]
    }
    try:
        print("reqest")
        response = requests.post(url, headers=header, json=body)
        print('Google cloud response:  '+ str(response.status_code))
        response = response.json()
        #print (response)
        if len(response['responses'][0]) > 0:
            text = response["responses"][0]["textAnnotations"][0]["description"]
            length = len(text)
            for s in range(length):
                if ((s+1)<length-1) and ((s-1)>1) and (text[s] == '\n') and ((text[s+1]).isupper()==True):
                    text = text[:(s)] + ('. ') +text[(s+1):]
            text = text.replace('\n', ' ').replace('\r', ' ' )
            text = text.lower()  
        else:
            text = ''
    except KeyError:
        text = ''
    return(text)
def OCR():
    path = ('image.jpg')
    with io.open(path, 'rb') as image_file:
        content = encode_image(image_file)
    print("start")
    text=(document_ocr(content))
    print("xong")
    print(text)
    return(text)