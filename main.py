"""
Advanced Voice Processing Module for AI Voice Assistant
=====================================================

This module provides enterprise-grade voice processing capabilities including
speech-to-text conversion, audio preprocessing, and real-time voice analysis.

Features:
- High-accuracy speech recognition with Google Speech API
- Audio preprocessing and noise reduction
- Real-time voice activity detection
- Multi-format audio support (WAV, MP3, M4A)
- Conversation context preservation
"""


# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from twilio.twiml.voice_response import VoiceResponse
from assistant import handle_conversation
import uvicorn
import os

app = FastAPI()

# Ensure static directory exists
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/answer-call", response_class=PlainTextResponse)
async def answer_call():
    resp = VoiceResponse()
    resp.say("Hi, I’m your AI assistant. Please speak after the beep.")
    resp.record(
        action="/process-recording",
        method="POST",
        max_length=10,  # reduced from 15 to speed up turnaround
        play_beep=True,
        timeout=3  # shorter silence timeout
    )
    return str(resp)

@app.post("/process-recording", response_class=PlainTextResponse)
async def process_recording(RecordingUrl: str = Form(...)):
    audio_url, should_hang_up = handle_conversation(RecordingUrl)
    resp = VoiceResponse()
    resp.play(audio_url)

    if should_hang_up:
        resp.hangup()
    else:
        resp.redirect("/answer-call")  # continue loop

    return str(resp)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

