import speech_recognition as sr
def STT():
    r = sr.Recognizer()
    with sr.Microphone() as source: # Specify which input device to use
        print("Say something!")
        audio = r.listen(source)
    print ('OK')

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text=(r.recognize_google(audio,language='vi-VN'))
        if (text==""):
            return "NONE"
        text=text.lower()
        print('STT: '+text)
        return text
    except sr.UnknownValueError:
        return ("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        return ("Could not request results from Google Speech Recognition service; {0}".format(e))
