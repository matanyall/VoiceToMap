import re
import subprocess
import speech_recognition as sr
from FindAddressMap import make_map
import os
from subprocess import DEVNULL, STDOUT

# os.system('export GOOGLE_APPLICATION_CREDENTIALS="/home/matanya/Documents/GitHub/flight-knowledge-engine-15d3388253f2.json"')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/matanya/Documents/GitHub/flight-knowledge-engine-15d3388253f2.json"
subprocess.Popen(["/usr/bin/python3", "-m", "http.server"], shell=False, stdout=DEVNULL, stderr=STDOUT)
# os.system('python3 -m http.server')
# Regex for getting the address out of speech string
street_address = re.compile('\d{1,5} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)', re.IGNORECASE)
# Initializers for SpeechRecognition
r = sr.Recognizer()
mic = sr.Microphone()
result = ""

# main loop
with mic as source:
    # Microphone is set as source for speech-to-text engine, and slight calibration for ambient noise
    print("quiet for calibration:")
    r.adjust_for_ambient_noise(source) 
    print("Ready:")
    # loop that runs 
    while True:
        audio = r.listen(source)
        try:
            result = r.recognize_google_cloud(audio, language="en-US")
            print(result)
        except sr.UnknownValueError:
            nothing = None
            # print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if result:
            # print(result)
            if re.search(street_address, result):
                address = re.search(street_address, result).group(0)
                print("Address found: " + address)
                make_map(address)
        result = ""