'''
Hello!
'''
import speech_recognition as sr

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    print('Start talking now!')
    with mic as source:
        audio = r.listen(source)

    recognized_audio = r.recognize_google(audio)
    print('You said: ' + recognized_audio)

if __name__ == '__main__':
    main()
