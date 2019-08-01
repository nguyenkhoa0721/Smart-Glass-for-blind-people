import requests
from IPython.display import HTML

def camxuc(cx):
    switcher = [
        ("anger","tức giận"),
        ("contempt","coi thường"),
        ("disgust","ghê tởm"),
        ("fear","sợ hãi"),
        ("happiness","hạnh phúc"),
        ("neutral","lo lắng"),
        ("sadness","buồn bã"),
        ("surprise","bất ngờ")
    ]
    i=-1
    while (i<=7):
        i=i+1
        if(cx==switcher[i][0]):
            return switcher[i][1]
def FACEDES(text):
    
    pathToFileInDisk = r'/media/nk/Work/smartglass_cloud/image.jpg'
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()
    
    subscription_key = "362e0fd98a244504b3ac00c573cb3e66"
    assert subscription_key
    face_api_url = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/detect'
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = subscription_key
    headers['Content-Type'] = 'application/octet-stream'
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,noise'
    }
    json=None
    try:
        response = requests.post(face_api_url, params=params, headers=headers, json=json,data=data)
        face = response.json()
    except:
        return ("ko tim thay mat")
    i=0
    gender=[]
    age=[]
    emotion=[]
    emotions=["anger","contempt","disgust","fear","happiness","neutral","sadness","surprise"]
    while 1:
        try:
            #gioi tinh
            gender.append(face[i]["faceAttributes"]["gender"])
            if (gender[i]=="female"):
                gender[i]="nữ"
            else:
                gender[i]="nam"
            #tuoi
            age.append(int(face[i]["faceAttributes"]["age"]))
            #camxuc
            tmp=0.0
            emotion.append("none")
            for tmpemotion in emotions:
               #print (face[i]["faceAttributes"]["emotion"][tmpemotion])
               if (tmp<float(face[i]["faceAttributes"]["emotion"][tmpemotion])):
                   tmp=float(face[i]["faceAttributes"]["emotion"][tmpemotion])
                   emotion[i]=tmpemotion
                   print(tmp)
            emotion[i]=camxuc(emotion[i])
            i=i+1
        except:
            break
    if (text=="tuoi"):
        text="số tuổi: "
        for agee in age:
            text=text+str(agee)+","
        return text
    if (text=="gioitinh"):
        text="giới tính: "
        for genderr in gender:
            text=text+genderr+","
        return text
    if (text=="camxuc"):
        text="cảm xúc là: "
        for emotionn in emotion:
            text=text+emotionn+","
        return text
    if (text=="all"):
        text=""
        for i in range(len(age)):
            text=text+gender[i]+", khoảng "+str(age[i])+" tuổi, đang "+emotion[i]+"."
        return text