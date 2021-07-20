# import MapHTMLGen
# import VoiceToToken
import re
import speech_recognition as sr
import time
from FindAddressMap import make_map
import os

os.system('export GOOGLE_APPLICATION_CREDENTIALS="/home/matanya/Documents/GitHub/flight-knowledge-engine-15d3388253f2.json"')
# os.system('python3 -m http.server')
# Regex for getting the address out of speech string
street_address = re.compile('\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)', re.IGNORECASE)
# Initializers for SpeechRecognition
r = sr.Recognizer()
mic = sr.Microphone()
result = ""

# main loop
with mic as source:
    # Microphone is set as source for speech-to-text engine, and slight calibration for ambient noise
    print("quiet for calibration")
    r.adjust_for_ambient_noise(source) 
    print("System is calibrated, you can talk now")
    # loop that runs 
    while True:
        audio = r.listen(source)
        try:
            result = r.recognize_google_cloud(audio, language="en-US")
            print(result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if result:
            # print(result)
            if re.search(street_address, result):
                address = re.search(street_address, result).group(0)
                print("Address found: " + address)
                make_map(address)
        result = ""





# def callback(recognizer, audio):
#     # received audio data, now we'll recognize it using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         transcript2 = recognizer.recognize_google(audio)
#         print("Text: " + transcript2)
#         set_transcript(transcript2)
#         # return transcript
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#         transcript2 = "Error"
#         set_transcript(transcript2)
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))




# transcript = ""

# with mic as source:
#     r.adjust_for_ambient_noise(source) 
#     res2 = ""
# stop_listening = r.listen_in_background(mic, callback)


# for _ in range(500): time.sleep(0.1)
# print("Transcript: " + str(transcript))

# while True:
#     res2 = get_transcript()
#     if res2:
#         print("In main.py: " + res2)

# while True:
#     token = get_token()
#     map_update(token)
    


