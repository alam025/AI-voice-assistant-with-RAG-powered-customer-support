# assistant.py
from gpt_test import chat_with_gpt
from tts_test import speak_and_get_url
from voice_test import listen

EXIT_PHRASES = ["goodbye", "thank you", "bye", "exit", "stop"]

def handle_conversation(recording_url):
    caller_input = listen(recording_url)
    print("User said:", caller_input)

    if caller_input:
        for phrase in EXIT_PHRASES:
            if phrase in caller_input.lower():
                final_response_url = speak_and_get_url("You're welcome! Goodbye.")
                return final_response_url, True  # Tell main to hang up

        ai_response = chat_with_gpt(caller_input)
        print("AI:", ai_response)
        return speak_and_get_url(ai_response), False

    return speak_and_get_url("Sorry, I didn’t catch that. Could you repeat?"), False
