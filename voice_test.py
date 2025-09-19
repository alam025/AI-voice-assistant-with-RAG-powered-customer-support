import requests
import speech_recognition as sr
import os, tempfile
from pydub import AudioSegment

TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN
TWILIO_SID = TWILIO_SID

def listen(recording_url):
    if not recording_url.endswith(".wav"):
        recording_url += ".wav"
    response = requests.get(recording_url, auth=(TWILIO_SID, TWILIO_AUTH_TOKEN))
    if response.status_code != 200:
        print("Error downloading recording:", response.text)
        return ""
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name

    recognizer = sr.Recognizer()
    with sr.AudioFile(tmp_file_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)  # ✅ Speed + clarity
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        print("User said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    finally:
        os.remove(tmp_file_path)
