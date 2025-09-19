# tts_test.py
import requests
import os, uuid

ELEVENLABS_API_KEY = ELEVENLABS_API_KEY
VOICE_ID = VOICE_ID 
NGROK_URL = NGROK_URL  # No spaces!

def speak_and_get_url(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }

    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()

    os.makedirs("static", exist_ok=True)
    fname = f"resp_{uuid.uuid4().hex}.mp3"
    path = os.path.join("static", fname)
    with open(path, "wb") as f:
        f.write(resp.content)

    return f"{NGROK_URL}/static/{fname}"
