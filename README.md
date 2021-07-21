# VoiceToMap

Voice to map is a program that takes voice as input and continually updates a map with the last address that is heard. The point is to expedite service availability in a call center for a fiber network provider.

## Installation

Before you can run this program on your own, you will need a Google Cloud API key (for Google Maps Geocode and gmplot), as well as Google Service Key (for Cloud Speech-To-Text). Without both this program will not work, as virtually all the functionality is implemented in the Google Cloud.

You then need to change where VoiceToMap looks for your keys. For development purposes I left them outside the repository, so I don't accidentally push them to Github (again).

The locations for each key are specified in the following places:

main.py:
```python
9:  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<service key .json absolute file path>"
```
FindAddressMap.py:
```python
5:  APIKey_Addr = "<file path to API key in a .txt file>"
```
Now, we can start the rest of the setup. This program does not include an example html file, so right now it's a bit of a pain. I'm working on streamlining this, so I won't talk about it here. However, I will give a high level explanation of how it works.

## How it works

1. User starts talking
2. SpeechRecognition listens on the microphone for speech
3. Audio is sent to Google with Cloud Speech-To-Text
4. VoiceToMap looks at returned string for what looks like an address with a Regex
5. Extracted address is then sent to FindAddressMap
6. Address is turned into coordinates with Google Geocode
7. gmplot generates html file with map and marker centered on coordinate
8. Live.js script is added to html file
9. Pythons http.server creates local network that points to html file
10. Browser opens 'localhost:8000/address_map_file.html'

Because live.js is running in the browser, the page refreshes every time the html file changes, leading to an update of the map.

## Packages Needed

* PyAudio
* PortAudio
* SpeechRecognition
* gmplot
* googlemaps
* google-api-core
* google-auth
* google-api-python-client

## Pictures

Coming soon!

## License
[MIT](https://choosealicense.com/licenses/mit/)