#be able to communicate with Turing to help out on different things
import speech_recognition as sr
import pyaudio
import webbrowser
from time import ctime
import playsound
import os
import random
from gtts import gTTS
import time


r=sr.Recognizer()

def record_audio(ask = False):
    #source is the input from microphone
    with sr.Microphone() as source:
        #audio variable is based on source
        if ask:
            turing_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data= r.recognize_google(audio)
        #voice data variable is inputed using Google and passes the audio source through
        #if mic doesn't understand you
        except sr.UnknownValueError:
            turing_speak('Sorry, I did not get that')
        except sr.RequestError:
            turing_speak('Sorry sir. The servers are down. Trying to restart them now')
        return voice_data

def turing_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) +'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        turing_speak('I am Turing')
    if 'what time is it' in voice_data:
        turing_speak(ctime())
    if 'search' in voice_data:
        search= record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        turing_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location= record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        turing_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
turing_speak("What can I help you with?")
while 1:
    voice_data=record_audio()
    respond(voice_data)