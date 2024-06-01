from langdetect import detect
from googletrans import Translator

def detect_and_translate(text):
    try:
        # Detect the language of the input text
        detected_language = detect(text)
        
        # Check if the detected language is English
        if detected_language != 'en':
            # Initialize the translator
            translator = Translator()
            
            # Translate the text to English
            translation = translator.translate(text, src=detected_language, dest='en')
            return translation.text
        
        # If the text is already in English, return it as is
        return text
    
    except Exception as e:
        return f"Error detecting or translating text: {e}"
