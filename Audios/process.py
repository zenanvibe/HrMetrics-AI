import speech_recognition as sr
from fastapi import HTTPException

def extract_text(temp_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the audio file as the audio source
    with sr.AudioFile(temp_file_path) as source:
        audio_data = recognizer.record(source)

    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Audio unintelligible")
    except sr.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Could not request results; {e}")
    return text