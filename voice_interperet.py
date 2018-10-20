import speech_recognition as sr

def collect_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        try:
            audio = r.listen(source, timeout=10.0)
        except:
            return '[NO INPUT]'

    try :
        recognized_audio = r.recognize_google(audio)
    except:
        recognized_audio = '[NO INPUT]'
    return recognized_audio