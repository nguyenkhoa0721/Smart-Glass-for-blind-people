import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
from google.cloud import vision
from google.cloud.vision import types
def GLABEL():
    client = vision.ImageAnnotatorClient()
    file_name = os.path.join(
        os.path.dirname(__file__),
        'image.jpg')
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    i=-1
    text=""
    for label in labels:
        i=i+1
        text=text+str(label.description)+","
        if (i==4):
            break
    return(text)

