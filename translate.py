import speech_recognition as sr         #speech recognition library to convert my voice
import pyttsx3                          #convert translated text into speech
from langdetect import detect           #language detection
from googletrans import Translator

#create a recognizer object, a translator object, and a Text-to-Speech object

#instances for recognizer, translator, and TTS
r = sr.Recognizer()
translator = Translator(service_urls=['translate.google.com'])
tts = pyttsx3.init()

while True:
    #use default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        #listen to audio and adjust ambient noise level
        r.adjust_for_ambient_noise(source)
        #record user speech input from mic
        audio = r.listen(source)
    try:
        # recognize speech using Google speech Recognition
        text = r.recognize_google(audio)
        input_language = detect(text)
        # translate speech to English if detected language is in Spanish
        if input_language == 'es':
            translation = translator.translate(text, src='es', dest='en')
            print(f"Translated to English: {translation.text}")
            # speak the translated text
            tts.say(translation.text)
            tts.runAndWait()            #block program execution until done
        # translate speech to Spanish if detected language is in English
        elif input_language == 'en':
            translation = translator.translate(text, dest='es')
            print(f"Translated to Spanish: {translation.text}")
            # speak the translated text
            tts.say(translation.text)
            tts.runAndWait()
        else:
            print("Language not supported") 
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")